# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 07:05:21 2021

@author: praja
"""
  ##### Descritization ###
  
  import pandas as pd
  
 data = pd.read_csv("C:\data\iris.csv")
 data.head()  # it gives quick preview of the data
 data.describe() # its shows statistical calculation on datasets ( count, 1st moment, 2nd moment.)
 
#Drop the unnamed variable which is not useful for calculation 

data.drop(['Unnamed: 6', ], axis=1, inplace=True) 
# inplace=True =change the value in the memory itself 
#axis=1 drop column and axis=0 drop row

# descritization for Sepal.Length column for that we use cut function


 d1 = data['Sepal_Length_binned '] = pd.cut( data['Sepal_Length'], bins=[4,5,6,8],labels=["setosa", "versicolor", "verginica"])

 d2 = data['Sepal_Width_binned '] = pd.cut( data['Sepal_Width'], bins=[2,3,4,5],labels=["verginica","versicolor","setosa"])

 d3 =  data['Petal_Length_binned'] = pd.cut(data['Petal_Length'], bins=[1,3,5,7],labels=["setosa", "versicolor", "verginica"])

 d4 =  data['Petal_Width_binned'] = pd.cut(data['Petal_Width'], bins=[0,1,2,3],labels=["setosa", "versicolor", "verginica"])

