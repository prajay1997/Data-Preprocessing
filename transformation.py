# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:01:52 2021

@author: praja
"""
## Transformation ##
import pandas as pd
import numpy as np
 # load the data
 data = pd.read_csv("C:\data\datasets_datapreprocessing\calories_consumed.csv")

data.columns
data.shape
data.isna().sum()
data.describe()

# As data has high magnitude difference so we normalise it.
# to scale the data between 0 to 1 we use Normalisation
 # define the custom function norm
 
 def norm_fun(i):
     x = (i-i.min())/(i.max()-i.min())
     return(x)
     
data_norm =norm_fun(data)
 data_norm.describe()

 # Normal Quantile-Quantile plot
 import scipy.stats as stats
 import pylab
 
 # Check whether data is normally distributed
 stats.probplot(data.Weight_gained_grams, dist="norm" ,plot=pylab)  # not normally distributed
 stats.probplot(data.Calories_Consumed, dist="norm", plot=pylab)    # not fully normally distributed
  # Lets transform the data so that variables gets normal
  
  import numpy as np
 stats.probplot(np.log(data.Weight_gained_grams), dist="norm", plot=pylab)
stats.probplot(np.log(data.Calories_Consumed), dist="norm", plot=pylab)
