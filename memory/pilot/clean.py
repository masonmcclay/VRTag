import os
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pingouin as pg
# from pg_config import *
import numpy.polynomial.polynomial as poly





def dataOrg(file, number):

	df = pd.read_csv(file, sep= "\t", header= None)

	sub_id_col = [number for i in range(48)]

	trial_col = [(i+1) for i in range(48)]

	day = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

	df.insert(0,"subject", sub_id_col, True)
	df.insert(1, "trial", trial_col, True)
	df.insert(11, "day", day, True)

	df.columns = ["subject","trial","null","pic_id","act_x","act_y","est_x","est_y","correct","dist","rt","day"]

	#df.to_csv(file + '.csv')

	#print(df)

	#pic = df.iloc[:,[0]]
 
	#day = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2']
	#print(len(day))
	#df['day'] = day

	#data = {'pic_id': [pic]}
	#print(dict)

	#pd.Series(data)
	#print(data)
	#index = [0,1,2,3,4,5,6,7,8,9]

	df_new = pd.DataFrame(df)
	#print(df_new)

	df_new.to_csv('subs.csv')
	#print(df)



def main():

	score = 1

	for files in os.listdir():

		if files.endswith('phase3.txt'):
			root = str(files)
			print (root)
			clean = dataOrg(root, score)

	score+=1

main()