# -*- coding: utf-8 -*-
"""ParkinsonsF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s3XtbUjgPp9yDwdJZbWpwC5Yy5jsF-6E
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection & Analysis"""

parkinsons_data = pd.read_csv('parkinsons.csv')

#returns tuple(number of rows, number of columns)
parkinsons_data.shape

#dataset summary
parkinsons_data.info()

#sum of missing values 
parkinsons_data.isnull().sum()

#summary statistical description (count, mean, sd , min, median, 75th %, max)
parkinsons_data.describe()

# count of unique values in the 'status' column
parkinsons_data['status'].value_counts()



"""1  --> Parkinson's Positive

0 --> Healthy

"""

parkinsons_data.groupby('status').mean()


"""Data Pre-Processing

Separating the features & Target
"""

X = parkinsons_data.drop(columns=['name','status'], axis=1)
Y = parkinsons_data['status']

print(X)

print(Y)


"""Splitting the data to training data & Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training

Support Vector Machine Model
"""

model = svm.SVC(kernel='linear')

model.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Score
"""

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy score of training data : ', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy score of test data : ', test_data_accuracy)

"""Building a Predictive System"""

input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)


if (prediction[0] == 0):
  print("The Person does not have Parkinsons Disease")

else:
  print("The Person has Parkinsons")

"""Saving the trained model"""

import pickle

filename = 'parkinsons_model.sav'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open('parkinsons_model.sav', 'rb'))

for column in X.columns:
  print(column)

