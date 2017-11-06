import math
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:/Users/Josh/Downloads/AmesHousing.csv')

#print(df.tail())
df['SF'] = df['1st Flr SF']+df['2nd Flr SF']+df['Total Bsmt SF']

df = df[['Lot Frontage',  'Lot Area','SF','Overall Qual', 'Overall Cond', 'Year Built', 'Full Bath', 'Garage Area', 'SalePrice']]

print(df.head())

forecast_col = 'SalePrice'
df.dropna(inplace=True)

X = np.array(df[['Lot Frontage',  'Lot Area','SF','Overall Qual', 'Overall Cond', 'Year Built', 'Full Bath', 'Garage Area']])
y = np.array(df['SalePrice'])

X = preprocessing.scale(X)

print(X)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

for k in ['linear','poly','rbf','sigmoid']:
    clf = svm.SVR(kernel=k)
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print('SVM type confidence: ')
    print(k,confidence)

clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print('Linear Regression confidence: ')
print(confidence)
