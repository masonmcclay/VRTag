import os
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pingouin as pg
import numpy.polynomial.polynomial as poly
from matplotlib.patches import Patch


## Data visualization script for VRTag


## 1) Simple, non-object-oriented graphing. Good for by-subject graphing (excluding manipulation condition)


p1 = sns.color_palette("RdBu", n_colors=2)


fig, ax = plt.subplots()


sns.set_style("ticks")
sns.set_context("talk")

df = pd.read_csv("VRTag_days.csv")

#df['daycond'] = df.day + df.cond.astype(str)

## Pointplot for simple, easy mean/sem visualization



df = df.groupby(['subject','day','condition']).mean().reset_index()

#sns.pointplot(x="day",y="dist", hue = "condition", ax=ax,palette = p1,data=df, dodge= True,ci=68)
sns.swarmplot(x="day",y="dist", hue = "condition", dodge= True, ax=ax,data=df, hue_order = ["video","vr"])


#ax.legend_.remove()
sns.despine(ax=ax)
<<<<<<< HEAD
ax.set(xlabel="Condition",ylabel="Day 1 minus Day 2 distance (pixels)")

ax.set(xlabel="Condition",ylabel="Distance from Correct (pixels)")

## box and swarm for specific data-point visualization

#sns.boxplot(x="day",y="dist",ax=ax,palette = p1,data=df, dodge= True)
#sns.swarmplot(x="day",y="dist",ax=ax,color = "black",data=df, dodge= True)


legend_elements = [Patch(facecolor=p1[0],edgecolor="black", label='VR'),
Patch(facecolor=p1[1],edgecolor='black', label='Control')]

plt.legend(handles=legend_elements,title='Day', loc = "best")





## 2) Object-oriented graphing. Good for across-subjects, by-condition graphing


fig, ax = plt.subplots(1,2, sharey=True)

p2 = sns.color_palette("RdBu", n_colors=2)

df['daycond'] = df.day + df.cond.astype(str)

#order = [2,3,1,0]
#p2 = [p2[i] for i in order]

for i, cons in enumerate(con.confidence.unique()):

	sns.boxplot(x="proc",y="score",hue="daycond", col="confidence",order = ["view", "suppress"],ax=ax[i], palette = p2, data=con.query("confidence == @cons"), dodge= True, ci= 68)
	
	ax[i].legend_.remove()
	sns.despine(ax=ax[i])
	ax[i].set_title("%s confidence"%(cons))


	ax[i].hlines(0,ax[i].get_xlim()[0],ax[i].get_xlim()[1])
	ax[i].set(xlabel="Procedure",ylabel="Corrected Recognition")


legend_elements = [Patch(facecolor=p1[0],edgecolor="black", label='Day 1'),
Patch(facecolor=p1[1],edgecolor='black', label='Day 2')]

plt.legend(handles=legend_elements,title='Day', loc = "best")
