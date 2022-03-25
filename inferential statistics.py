# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 07:05:22 2021

@author: praja
"""

# Inferential Statistics Assignment 
# Q)5


import pandas as pd
# load the data
 data = pd.read_excel("C:\data\Assignment_module02 (1).xlsx")
 data.info()
data.isna().sum()

# Exploratory data Analysis
# Measures of Central Tendency/First moment business decision

data.Points.mean()     # '.' is used to refer to the variables within object
data.Points.median()
data.Points.mode()

data.Score.mean()
data.Score.median()
data.Score.mode()

data.Weigh.mean()
data.Weigh.median()
data.Weigh.mode()

from scipy import stats

stats.mode(data.Points)
stats.mode(data.Score)
stats.mode(data.Weigh)

# Measures of Dispersion / Second moment business decisions 

data.Points.var()     # Variance
data.Points.std()     # standard deviation
range = max(data.Points) - min(data.Points)  # range 

data.Score.var()     
data.Score.std()     
range = max(data.Score) - min(data.Score)

data.Weigh.var()     
data.Weigh.std()     
range = max(data.Weigh) - min(data.Weigh)

data.Points.skew()
data.Score.skew()
data.Weigh.skew()


# Q)7 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\data\df.csv")
df.describe()
df.info()

plt.bar(height=df.measure_x_in_percentage, x=np.arange(1,3,1))

plt.hist(df.measure_x_in_percentage)
plt.boxplot(df.measure_x_in_percentage)

# here 1 outlier if found which is 91.36
# calculate the measures of centrality 

df.measure_x_in_percentage.mean()
df.measure_x_in_percentage.median()
df.measure_x_in_percentage.mode()

# measures of Dispersion
df.measure_x_in_percentage.var()
df.measure_x_in_percentage.std()

df.measure_x_in_percentage.skew()
df.measure_x_in_percentage.kurt()

import seaborn as sns

df['measure_x_in_percentage'].hist(grid=False)
sns.distplot(df['measure_x_in_percentage'], hist=True)
 
# data is positively skewed.