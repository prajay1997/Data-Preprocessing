# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:23:27 2021

@author: praja
"""n
import pandas as pd
import numpy as np

## Standerdization##
from sklearn.preprocessing import StandardScaler
# load the dataset
data = pd.read_csv("C:\data\Seeds_data.csv")
data.describe()         # it gives five pointers (EDA)
a =data.describe()
scaler = StandardScaler()  # Initialise the scaler
data_sd = scaler.fit_transform(data)    # array format
# convert array back to dataframe
dataset = pd.DataFrame(data_sd)
result = dataset.describe()

## Normalisation ##
# load the dataset
data = pd.read_csv("C:\data\Seeds_data.csv")
 data.columns
 a =data.describe()
 # Normalisation Function # custom function
 # Range Converts to 0 to 1
 
 def norm_fun(i):
     x = (i-i.min())/(i.max()-i.min())
     return(x)

data_norm = norm_fun(data)
b = data_norm.describe

# Normal Quantile-Quantile plaot

import scipy.stats as stats
import pylab

data = pd.read_csv("C:\data\Seeds_data.csv")
data.columns
# checking whether data is normally distributed

stats.probplot(data.Area, dist="norm", plot=pylab)
stats.probplot(data.Perimeter, dist="norm", plot=pylab)
stats.probplot(data.Compactness, dist="norm", plot=pylab)
stats.probplot(data.length, dist="norm", plot=pylab)
stats.probplot(data.Width, dist="norm", plot=pylab)
stats.probplot(data.Assymetry_coeff, dist="norm", plot=pylab)
stats.probplot(data.len_ker_grove, dist="norm", plot=pylab)
stats.probplot(data.Perimeter, dist="norm", plot=pylab)

# Transformation to make variables normal

import numpy as np
stats.probplot(np.sqrt(data.Area), dist="norm",plot=pylab)
stats.probplot(np.log(data.Perimeter),dist="norm", plot=pylab)
stats.probplot(1/(data.Compactness),dist="norm", plot=pylab)
stats.probplot(1/(data.length), dist="norm", plot=pylab)
stats.probplot(1/(data.Width), dist="norm", plot=pylab)
stats.probplot(np.sqrt(data.Assymetry_coeff), dist="norm", plot=pylab)
stats.probplot(np.sqrt(data.len_ker_grove), dist="norm", plot=pylab)



