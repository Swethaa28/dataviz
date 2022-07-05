# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zL9kYrJ52ixIfecsmHfE0dq1RQPqgLcQ

NAME : SWETHA
"""

#Importing the Libraries required for the problem
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv('/content/clustering.csv - clustering.csv.csv')

data

data.shape

data.info

data.head(10)

data.describe()

#Visualizing the data
sns.set_style('darkgrid')
sns.scatterplot(y=data['ApplicantIncome'],x=data['CoapplicantIncome'])
plt.title('ApplicantIncome vs CoapplicantIncome ',size=50)
plt.xlabel('ApplicantIncome')
plt.ylabel('CoapplicantIncome')
plt.show()

#Visualizing the data
sns.set_style('darkgrid')
sns.scatterplot(y=data['LoanAmount'],x=data['Credit_History'])
plt.title('LoanAmount vs Credit_History',size=50)
plt.xlabel('LoanAmount')
plt.ylabel('Credit_History')
plt.show()

#From the above graph, we can see a positive linear relation between the hours studied and the percentage obtained(score).

#Training the Model

#1. Preparing the Data

X =data.iloc[:, :-1].values  
y =data.iloc[:, 1].values

#the next step is to split this data into training and test sets.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X, y,test_size=0.2, random_state=0)

sns.scatterplot("ApplicantIncome",'CoapplicantIncome',data=data)

a=data.corr()
a

from sklearn.model_selection import train_test_split as tt
x=data.drop(columns=['LoanAmount'])
x

x_train,x_test,y_train,y_test=tt(x,y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()

import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn import datasets, model_selection
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns

data = datasets.load_iris()

X = data['data']
y = data['target']
print(X.shape)
print(y.shape)

#the next step is to split this data into training and test sets.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X, y,test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train) 
print("Training complete.")

#Predicting the % score
print(X_test)
y_pred = regressor.predict(X_test)

#Comparing the result with acutal data
df= pd.DataFrame({'ACTUAL' : y_test, 'PREDICTION' : y_pred})
df

#Evaluating the Model(Accuracy)
from sklearn import metrics  
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred))

# importing LinearRegression
from sklearn.linear_model import LinearRegression

#creating an object for LinearRegression
model = LinearRegression()

# fitting the model
model.fit(X_train, y_train)

#Making Predictions
# testing the model
y_pred = model.predict(X_test)

#checking accuracy of our model
data = pd.DataFrame({"Actual" : y_test,"Predicted":y_pred})
print(data)

#Evaluating the model
from sklearn import metrics as mts

#mean abolute error
mean_abs_error = mts.mean_absolute_error(y_test,y_pred)

print("Mean Absolute Error : ",mean_abs_error)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

model = Sequential()

model.add(LSTM(units=50,return_sequences=True,input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))

model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50))
model.add(Dropout(0.2))

model.add(Dense(units=1))

model.compile(optimizer='adam',loss='mean_squared_error')

model.fit(X_train,y_train,epochs=5,batch_size=32)

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import sklearn.metrics as sm
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report

iris= pd.read_csv('/content/clustering.csv - clustering.csv.csv')

iris.info()

iris.describe()

plt.scatter(iris['Loan_Amount_Term'],iris['Credit_History'])

sns.pairplot(iris, hue='LoanAmount')

sns.pairplot(iris, hue="ApplicantIncome", diag_kind="CoapplicantIncome	")

iris.corr()

sns.heatmap(iris.corr(), cmap="RdPu")

target=iris['ApplicantIncome']
df=iris.copy()
df=df.drop('ApplicantIncome', axis=1)
df.shape

x=iris.iloc[:, [0,1,2,3]].values
LaEn=LabelEncoder()
iris['ApplicantIncome']=LaEn.fit_transform(iris['ApplicantIncome'])
y=iris['ApplicantIncome'].values
iris.shape

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print("Trainging set:",x_train.shape)
print("Testing set:",x_test.shape)