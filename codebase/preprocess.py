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


def dataOrg(file, number, out, source, meta):

	## Assigning values to necessary variables and dataframes

	print(number)

	df = pd.read_csv(file, sep= "\t", header= None)

	sub_id_col = [number for i in range(48)]

	trial_col = [(i+1) for i in range(48)]

	day = np.repeat([1,2],24)

	## for tiling:
	## np.tile([1,2],2)

	df.insert(0,"subject", sub_id_col, True)
	df.insert(1, "trial", trial_col, True)
	df.insert(11, "day", day, True)
	df.insert(12, "condition", True)

	df.columns = ["subject","trial","null","pic_id","act_x","act_y","est_x","est_y","correct","dist","rt","day", "condition"]

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

	dist_mean = np.mean(day1) - np.mean(day2)

	rt_mean = np.mean(day1rt) - np.mean(day2rt)

	df_mean = pd.DataFrame({'subject':[number],
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

	if number == 1:


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


	## read in metadata

	##meta_path = "C:/Users/mason/Desktop/VRTag/meta_data"

	##os.chdir(meta_path)

	##meta_df = pd.read_csv("meta_data.csv", sep= "\t", header= None)


	## Set to the working directory.

	path = "C:/Users/mason/Desktop/VRTag/memory/raw"

	## Set output directory.

	output = "C:/Users/mason/Desktop/VRTag/memory/preprocessed"


	## Assign sub cocatenation

	sub = 0

	os.chdir(path)

	for files in os.listdir():

		os.chdir(path)

		sub+=1

		print(sub)

		if files.endswith('phase3.txt'):
			root = str(files)
			print (root)
			clean = dataOrg(root, sub, output, path, meta_df)

	#sub+=1

main()