# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 08:52:26 2021

@author: praja
"""
# 1. outlier treatment

import pandas as pd                    # for data manipulation
import numpy as np                     # for arithmatic operations   
import seaborn as sns                  # For advance visualization    
  
data = pd.read_csv("C:\\data\\boston_data.csv")     # loading the data
data.dtypes                                         # to know the datatypes of each vaviable/column
data.describe()  # it gives  five point summary
data.info()
# lets find out the outlier in crim

sns.boxplot(data.crim)
sns.boxplot(data.zn)
sns.boxplot(data.indus)   # no outliers in indus column
sns.boxplot(data.chas)
sns.boxplot(data.nox)     # no outliers in nox column
sns.boxplot(data.rm)
sns.boxplot(data.age)     #  no outliers in age column
sns.boxplot(data.dis)
sns.boxplot(data.rad)     # no outliers in rad column
sns.boxplot(data.tax)     # no outliers in tax column
sns.boxplot(data.ptratio)
sns.boxplot(data.black)
sns.boxplot(data.lstat)
sns.boxplot(data.medv)

# lets remove the columns which don't have outliers

data.drop(['indus','nox','age','rad','tax'],axis=1, inplace=True)

# Detection of outliers (find limits for crim based on IQR)
# quantile function = it gives the value at the given quantile say between 0 to 1

IQR = data['crim'].quantile(0.75) - data['crim'].quantile(0.25)

lower_limit = data['crim'].quantile(0.25) -(IQR*1.5)

upper_limit = data['crim'].quantile(0.75) + (IQR*1.5)

# lets trim the dataset (remove )


Outliers_crim = np.where(data['crim']> upper_limit, True, np.where(data['crim']<lower_limit,True, False))
 # it gives outliers value+ True else false
 sum(Outliers_crim)

data_trimmed = data.loc[~(Outliers_crim),] # non outliers selected and outliers deleted 
data.shape
data_trimmed.shape


sns.boxplot(data_trimmed.crim)

# because of trimming dataloss happens so we do replacement or winsorisation
# replace the outliers by maximum and minimum limit

data['data_replaced']= pd.DataFrame(np.where(data['crim']>upper_limit,upper_limit, np.where(data['crim']<lower_limit,lower_limit, data['crim'])))

sns.boxplot(data.data_replaced)

# winsorisation #
 
# For Winsorisation we have to install package called feature_engine

pip install feature_engine
  from feature_engine.outliers import Winsorizer
winsor = Winsorizer( capping_method = 'iqr',
                           tail          = 'both',
                           fold          =  1.5,
                           variables = ['crim'])

# lets transform the data / apply the function to the data


data_crim = winsor.fit_transform(data[['crim']])
sns.boxplot(data_crim.crim)

# outlier treatment  for zn column

IQR = data['zn'].quantile(0.75)-data['zn'].quantile(0.25)

lower_limit = data['zn'].quantile(0.25) -(IQR*1.5) 

upper_limit = data['zn'].quantile(0.75) + (IQR*1.5)      


# lets flag the outliers in the dataset

outlier_zn = np.where(data['zn']>upper_limit,True, np.where(data['zn']<lower_limit,True, False))
sum(outlier_zn)
 # trimming
 
 data_trimmed1 = data.loc[~(outlier_zn),]
 
 data.shape 
 data_trimmed1.shape
 
 sns.boxplot(data_trimmed1.zn)

#  data loss happens so we do replace or winsorisation
# replace the outliers with maximum and minimum limit

data['data_replaced']=pd.DataFrame(np.where(data['zn']>upper_limit,upper_limit, np.where(data['zn']<lower_limit,lower_limit, data['zn'])))
sns.boxplot(data.data_replaced)

# winsorization

pip install feature_engine
from feature_engine.outliers import Winsorizer
winsor1 = Winsorizer( capping_method = 'iqr',
                           tail          = 'both',
                           fold          =  1.5,
                           variables = ['zn'])


data_zn = winsor1.fit_transform(data[['zn']])
sns.boxplot(data_zn.zn)

### outlier treatment for "rm" column

IQR = data['rm'].quantile(0.75) - data['rm'].quantile(0.25)
lower_limit = data['rm'].quantile(0.25) -  (IQR*1.5)                                                    
upper_limit = data['rm'].quantile(0.75) + (IQR*1.5)

#lets flag the outliers in the dataset ('rm' column)
outliers_rm = np.where(data['rm']>upper_limit,True, np.where(data['rm']<lower_limit,True,False))
sum(outliers_rm)
# trimming of ouliers
 data_trimmed2 = data.loc[~(outliers_rm),]
data.shape
data_trimmed2.shape
sns.boxplot(data_trimmed2.rm)
# Replacement # Replace the outliers by the maximum and minimum  limit

data['data_replaced'] = pd.DataFrame(np.where(data['rm']>upper_limit,upper_limit,np.where(data['rm']<lower_limit,lower_limit,data['rm'])))
sns.boxplot(data.data_replaced)

# Winsorization
pip install feature_engine
from feature_engine.outliers import Winsorizer

winsor = Winsorizer( capping_method = 'iqr',
                    tail ='both',
                    fold =1.5,
                    variables = ['rm'])
# fit the data for which winsorization is to be done
data_rm = winsor.fit_transform(data[['rm']])
sns.boxplot(data_rm.rm)

# oulier treatment for 'dis' column

IQR = data['dis'].quantile(0.75) - data['dis'].quantile(0.25)
lower_limit = data['dis'].quantile(0.25) - (IQR*1.5)
upper_limit  = data['dis'].quantile(0.75) + (IQR*1.5)

# flag the outlier for 'dis'column
outlier_dis = np.where(data['dis']>upper_limit,True, np.where(data['dis']<lower_limit,True,False))
sum(outlier_dis)

# trimming the data
data_trimmed3 = data.loc[~(outlier_dis),]

sns.boxplot(data_trimmed3.dis)

# data losss happens so we replacement with maximum and minimum values

data['data_replaced']= pd.DataFrame(np.where(data['dis']>upper_limit,upper_limit, np.where(data['dis']<lower_limit,lower_limit,data['dis'])))
sns.boxplot(data.data_replaced)

# winsorization #
 pip install feature_engine
from feature_engine.outliers import Winsorizer 
winsor = Winsorizer(capping_method = 'iqr',
                      tail = 'both',
                     fold = 1.5,
                     variables = ['dis'])
data_dis = winsor.fit_transform(data[['dis']])
sns.boxplot(data_dis.dis)

## outlier treatment for prt ratio column ##

# #Detection of outliers (find limits for crim based on IQR)
# quantile function = it gives the value at the given quantile say between 0 to 1

IQR = data['ptratio'].quantile(0.75) - data['ptratio'].quantile(0.25)
lower_limit = data['ptratio'].quantile(0.25) - (IQR*1.5)
upper_limit = data['ptratio'].quantile(0.75) + (IQR*1.5)

# flag the outlier #
outliers_ptratio = np.where(data['ptratio']>upper_limit,True, np.where(data['ptratio']<lower_limit, True,False))
sum(outliers_ptratio)


# Trimming the data 
data_trimmed4 =  data.loc[~(outliers_ptratio),]
data.ptratio.shape
data_trimmed4.ptratio.shape

sns.boxplot(data_trimmed4.ptratio)

# trimming causes data loss so to avoid it replace the data

data['data_replaced']= pd.DataFrame(np.where(data['ptratio']>upper_limit,upper_limit,np.where(data['ptratio']<lower_limit,lower_limit, data['ptratio'])))
 sns.boxplot(data.data_replaced)
 
 # Winsorization#
 pip install feature_engine
from feature_engine.outliers import Winsorizer

winsor = Winsorizer( capping_method ='iqr',
                        tail = 'both',
                        fold = 1.5,
                        variables = ['ptratio'])
 data_ptratio = winsor.fit_transform(data[['ptratio']])
 sns.boxplot(data_ptratio.ptratio)
 
 ## outlier treatment for 'black column ##

# #Detection of outliers (find limits for crim based on IQR)
# quantile function = it gives the value at the given quantile say between 0 to 1
 sns.boxplot(data.black)
IQR = data['black'].quantile(0.75) - data['black'].quantile(0.25)
lower_limit = data['black'].quantile(0.25) - (IQR*3)
upper_limit = data['black'].quantile(0.75) + (IQR*3)

# flag the outlier #
outliers_black = np.where(data['black']>upper_limit,True, np.where(data['black']<lower_limit, True,False))
sum(outliers_black)



# Trimming the data 
data_trimmed5 =  data.loc[~(outliers_black),]
data.black.shape
data_trimmed5.black.shape

sns.boxplot(data_trimmed5.black)

# trimming causes data loss so to avoid it replace the data

data['data_replaced']= pd.DataFrame(np.where(data['black']>upper_limit,upper_limit,np.where(data['black']<lower_limit,lower_limit, data['black'])))
 sns.boxplot(data.data_replaced)
 
 # Winsorization#
 pip install feature_engine
from feature_engine.outliers import Winsorizer

winsor = Winsorizer( capping_method ='iqr',
                        tail = 'both',
                        fold = 3,
                        variables = ['black'])
 data_black = winsor.fit_transform(data[['black']])
 
sns.boxplot(data_black.black)

# outlier treatment for lstat column#
sns.boxplot(data.lstat)

IQR = data['lstat'].quantile(0.75) - data['lstat'].quantile(0.25)
lower_limit = data['lstat'].quantile(0.25) - (IQR*1.5)
upper_limit = data['lstat'].quantile(0.75) + (IQR*1.5)

# flag the outliers
outliers_lstat = np.where(data['lstat']>upper_limit,True, np.where(data['lstat']<lower_limit,True,False))                                            
sum(outliers_lstat) 

# trimming the outliers
data_trimmed6 = data.loc[~(outliers_lstat),]
data.shape
data_trimmed6.shape
sns.boxplot(data_trimmed6.lstat)

# Replace the data with min and max 
data['data_replaced']=pd.DataFrame(np.where(data['lstat']>upper_limit,upper_limit, np.where(data['lstat']<lower_limit,lower_limit, data['lstat'])))
sns.boxplot(data.data_replaced)

#Winsorization#

pip install feature_engine
from feature_engine.outliers import Winsorizer

winsor = Winsorizer(capping_method = 'iqr',
                    tail = 'both',
                    fold =  1.5,
                    variables = ['lstat'])
data_lstat = winsor.fit_transform(data[['lstat']])
sns.boxplot(data_lstat.lstat)


# outlier treatment for medv column #
sns.boxplot(data.medv)

IQR = data['medv'].quantile(0.75) - data['medv'].quantile(0.25)
lower_limit = data['medv'].quantile(0.25) - (IQR*1.5)
upper_limit = data['medv'].quantile(0.75) + (IQR*1.5)

# flag the outliers
outliers_medv = np.where(data['medv']>upper_limit,True, np.where(data['medv']<lower_limit,True,False))                                            
sum(outliers_medv) 

# trimming the outliers
data_trimmed7 = data.loc[~(outliers_medv),]
data.shape
data_trimmed7.shape
sns.boxplot(data_trimmed7.medv)
# Replace the data with min and max 
data['data_replaced']=pd.DataFrame(np.where(data['medv']>upper_limit,upper_limit, np.where(data['medv']<lower_limit,lower_limit, data['medv'])))
sns.boxplot(data.data_replaced)

#Winsorization#

pip install feature_engine
from feature_engine.outliers import Winsorizer

winsor = Winsorizer(capping_method = 'iqr',
                    tail = 'both',
                    fold =  1.5,
                    variables = ['medv'])
data_medv = winsor.fit_transform(data[['medv']])
sns.boxplot(data_medv.medv)

##### The End######


