# -*- coding: utf-8 -*-
"""irisTask1.OIBSIP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E8b55wBVvPghXOivHV9cxAu1l8-Y8b0q
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore")

#Import iris dataset
df = pd.read_csv('Iris.csv')

df

df.info()

#checking for null values
df.isnull().sum()

df.columns

print(df.describe())

#Drop unwanted columns
df=df.drop(columns="Id")

df

df['Species'].value_counts()

x=df.iloc[:,:4]
y=df.iloc[:,4]

x

y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)

x_train.shape

x_test.shape

y_train.shape

y_test.shape

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

y_pred

from sklearn.metrics import accuracy_score,confusion_matrix
confusion_matrix(y_test,y_pred)

accuracy=accuracy_score(y_test,y_pred)*100
print("Accuracy of the model is {:.2f}".format(accuracy))