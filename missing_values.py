# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

data = pd.read_csv("C:\data\claimants.csv")

#To check count of 'NA' in each column
data.isna().sum()
 data.columns

# craete an imputer object that fills 'na' values
#mean and meadian is use for contineous data
# mode is used for discrete data 
#for mean, median, mode imputation we can use SimpleImputer or data.fillna()

from sklearn.impute import SimpleImputer
 
mode_imputer = SimpleImputer(missing_values=np.nan,strategy='most_frequent')
data['CLMSEX']= pd.DataFrame(mode_imputer.fit_transform(data[['CLMSEX']]))
 data['CLMSEX'].isna().sum()

mode_imputer = SimpleImputer(missing_values=np.nan,strategy='most_frequent')
data["CLMINSUR"]= pd.DataFrame(mode_imputer.fit_transform(data[["CLMINSUR"]]))
 data["CLMINSUR"].isna().sum()
 
 mode_imputer = SimpleImputer(missing_values=np.nan,strategy='most_frequent')
data["SEATBELT"]= pd.DataFrame(mode_imputer.fit_transform(data[["SEATBELT"]]))
 data["SEATBELT"].isna().sum()
 
median_imputer = SimpleImputer(missing_values=np.nan, strategy="median")
data["CLMAGE"] = pd.DataFrame(median_imputer.fit_transform(data[["CLMAGE"]]))
data["CLMAGE"].isna().sum()


# By fillna() method
data["CLMSEX"] = data["CLMSEX"].fillna(data["CLMSEX"].mode()[0])
data["CLMSEX"].isna().sum()

data["CLMINSUR"] = data["CLMINSUR"].fillna(data["CLMINSUR"].mode()[0])
data["CLMINSUR"].isna().sum()

data["SEATBELT"]= data["SEATBELT"].fillna(data["SEATBELT"].mode()[0])
data["SEATBELT"].isna().sum()

data["CLMAGE"]= data["CLMAGE"].fillna(data["CLMAGE"].median())
data["CLMAGE"].isna().sum()

data.isna().sum()



