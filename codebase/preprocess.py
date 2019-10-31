import os
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pingouin as pg
import numpy.polynomial.polynomial as poly
import csv


## A preprocessing/data cleaning script for VRTag


def dataOrg(file, out, source, number):

	## Assigning values to necessary variables and dataframes


	df = pd.read_csv(file, sep= "\t", header= None)


	#subject = file[:9]
	#print(subject)
	#number.append(subject)
	#print(number)

	subject = file[:9]

	print(subject)

	sub_id_col = np.repeat(subject, 48)

	print(sub_id_col)

	trial_col = [(i+1) for i in range(48)]

	day = np.repeat([1,2],24)

	## for tiling:
	## np.tile([1,2],2)

	df.insert(0,"subject", sub_id_col, True)
	df.insert(1, "trial", trial_col, True)
	df.insert(11, "day", day, True)
	df.insert(12, "condition", True)
	df.insert(13, "act_quad", True)
	df.insert(14, "est_quad", True)
	df.insert(15, "diff_quad", True)

	df.columns = ["subject","trial","null","pic_id","act_x","act_y","est_x","est_y","correct","dist","rt","day", "condition", "act_quad","est_quad","diff_quad"]

	df_days = df.copy()


	## Now create dataframe with average differeance between Day 1 and Day 2 performance, with Day 1 performance to be used as
	## a regressor in analysis

	day = df['day'].tolist()

	dist = df['dist'].tolist()

	rt = df['rt'].tolist()

	day2 = [d for d in dist if day[dist.index(d)] == int(2)]
	day1 = [d for d in dist if day[dist.index(d)] == int(1)]


	day2rt = [t for t in rt if day[rt.index(t)] == int(2)]
	day1rt = [t for t in rt if day[rt.index(t)] == int(1)]


	day1_mean = np.mean(day1)
	day2_mean = np.mean(day2)

	day1rt_mean = np.mean(day1rt)
	day2rt_mean = np.mean(day2rt)

	dist_mean = np.mean(day2) - np.mean(day1)

	rt_mean = np.mean(day2rt) - np.mean(day1rt)

	est_quad = []
	act_quad = []

	for i in range(47):

		if (1500 >= df["act_x"][i]) & (df["act_x"][i] >= 750):

			if (750 >= df["act_y"][i]) & (df["act_y"][i]  >= 0):
				act_quad.append(1)

			if (1500 >= df["act_y"][i]) & (df["act_y"][i]  >= 750):
				act_quad.append(4)


		if (750 >= df["act_x"][i]) & (df["act_x"][i] >= 0):

			if (750 >= df["act_y"][i]) & (df["act_y"][i]  >= 0):
				act_quad.append(3)

			if (1500 >= df["act_y"][i]) & (df["act_y"][i]  >= 750):
				act_quad.append(2)


		if (1500 >= df["act_x"][i]) & (df["act_x"][i] >= 750):

			if (750 >= df["est_y"][i]) & (df["est_y"][i]>= 0):
				est_quad.append(1)

			if (1500 >= df["est_y"][i]) & (df["est_y"][i]>= 750):
				est_quad.append(4)


		if (750 >= df["act_x"][i]) & (df["act_x"][i] >= 0):

			if (750 >= df["est_y"][i]) & (df["est_y"][i] >= 0):
				est_quad.append(3)

			if (1500 >= df["est_y"][i]) & (df["est_y"][i] >= 750):
				est_quad.append(2)


	if len(act_quad) < 48:
		act_quad.append("NaN")

	if len(est_quad) < 48:
		est_quad.append("NaN")

	print(act_quad)
	print(est_quad)

	aq = pd.Series(act_quad)
	eq = pd.Series(est_quad)

	df_days["act_quad"] = aq
	df_days["est_quad"] = eq

	
	quad_diff = []

	for i in range(47):
		quad_differ = act_quad[i] - est_quad[i]
		quad_diff.append(quad_differ)

	if len(quad_diff) < 48:
		quad_diff.append("NaN")
		

	qd = pd.Series(quad_diff)
	df_days["quad_diff"] = qd

	df_mean = pd.DataFrame({'subject':[subject],
							'day 1 distance':[day1_mean],
							'day 2 distance':[day2_mean],
							'day 1 rt':[day1rt_mean],
							'day 2 rt':[day2rt_mean],
							'dist difference':[dist_mean],
							'rt difference':[rt_mean]})

	df_mean.insert(7, "condition", True)
	#df_mean.columns = ["subject", "difference", "condition"]
	
	os.chdir(out)

	## Write new dataframe by days to CSV

	if len(sub_id_col) == 1:


		df_days.to_csv('VRTag_days.csv')

		print(df_days)

	## Write new dataframe for difference to CSV

		df_mean.to_csv('VRTag_difference.csv')

		print(df_mean)

	else:

		with open('VRTag_days.csv', 'a') as f1:
			df_days.to_csv(f1, header=False)

		with open('VRTag_difference.csv', 'a') as f2:
			df_mean.to_csv(f2, header=False)

	os.chdir(source)
	

def main():


	## Set to the working directory.

	path = "/Users/mgm3684/Desktop/lab_experiments/VRTag/memory/raw/phase3"

	## Set output directory.

	output = "/Users/mgm3684/Desktop/lab_experiments/VRTag/memory/preprocessed"

	## Assign sub cocatenation

	#subList = []

	os.chdir(path)

	sub = 0


	for files in os.listdir():

		os.chdir(path)

		

		if files.endswith('phase3.txt'):
			root = str(files)
			
			#print (root)
			clean = dataOrg(root, output, path, sub)
			sub+=1

	#sub+=1

main()