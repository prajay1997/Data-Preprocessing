# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:31:37 2021

@author: praja
"""

### Creating Dummy variable ##

import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv("C:\\data\\animal_category.csv")
data.columns     # gives the column names
data.shape

# Lets drop the Index column which is trelevent data

data.drop(['Index'], axis=1, inplace=True)  # didn't use another variableand use inplace function as it will save the changes in memory itslef
 data.columns
# create dummy variables
data_new = pd.get_dummies(data) 

data_new_1 = pd.get_dummies(data,drop_first = True)  # it delete unnecessory column and fit in single column

# one hot encoding
from sklearn.preprocessing import OneHotEncoder

# creating instance of one hot encoder

enc = OneHotEncoder()   # initialising method
enc_data = pd.DataFrame(enc.fit_transform(data.iloc[:,1:]).toarray())

# label Encoder

from sklearn.preprocessing import LabelEncoder
# creating instance labelEncoder

labelencoder = LabelEncoder()

x = data.iloc[:,0:3] # data splits into input and output values
y = data['Types']
y = data.iloc[:,3:]
data.columns

x['Gender'] = labelencoder.fit_transform(x['Gender'])
x['Homly']  = labelencoder.fit_transform(x['Homly'])

# label encode y

y['Types'] = labelencoder.fit_transform(y)
y= pd.DataFrame(y)    # cahnging to dataframe so that we can concate with x

# concate x and y 
 data_new = pd.concat([x,y], axis=1)
 data_new.columns




  