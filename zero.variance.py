# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:31:39 2021

@author: praja
"""
# import the libraries
import pandas as pd
import numpy as np
 # import the data
 
 data = pd.read_csv("C:\data\Z_dataset.csv")
 
 # first five rows of the data
 data.head()

# we check the shape of the data
data.shape

 # check whether the missing values in the data
 data.isnull()    # there is no null value. 

# lets check the data types of the variable

data.dtypes 
 

 # lets drop the ID variables as it is Irelevant for Analysis
  data.drop(['Id'], axis=1,inplace= True)
  data.shape
  data.columns

  # lets check the variables with zero variance
data.var() 
data.std()

# square.length, square.breadth,rec.breadth variables have zero variance 
# rec.length have the variance = 3.11
# so we ignore the columns with zero variance.

data_new = data.drop(['square_length','square_breadth','rec_breadth'],axis=1)

data.square_length.skew()   # positively skewed
data.square_breadth.skew()  # positively skewed
data.rec_Length.skew()      # negatively skewed
data.rec_breadth.skew()     # negatively skewed

data.square_length.kurt()
data.square_breadth.kurt()
data.rec_Length.kurt()
data.rec_breadth.kurt()

