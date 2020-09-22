#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv('train.csv')
df.loc[df['Fare']>400, 'Fare'] = df['Fare'].median()

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna("S", inplace=True)

del df['Cabin']
del df['Ticket']

def get_title(name):
    if "." in name:
        return name.split(",")[1].split('.')[0].strip()
    else:
        return 'No title in name'

def shorter_titles(x):
    title = x['Title']
    if title in ['Capt', 'Col', 'Major']:
        return 'Officer'
    elif title in ['Jonkheer', 'Lady', 'Don', 'Sir', 'the Countess', 'Dona']:
        return 'Royalty'
    elif title == 'Mme':
        return 'Mrs'
    elif title in ['Mlle', 'Ms']:
        return 'Miss'
    else:
        return title    

titles = set([x for x in df.Name.map(lambda x: get_title(x))])
df['Title'] = df['Name'].map(lambda x: get_title(x))
df['Title'] = df.apply(shorter_titles, axis=1)
df.drop('Name', axis=1, inplace=True)

df.Sex.replace(('male', 'female'), (0, 1), inplace=True)
df.Embarked.replace(('S', 'C', 'Q'), (0, 1, 2), inplace=True)
df.Title.replace(('Mr', 'Miss', 'Mrs', 'Master', 'Dr', 'Rev', 'Royalty', 'Officer'), (0, 1, 2, 3, 4, 5, 6, 7), inplace=True)

corr = df.corr()
corr.Survived.sort_values(ascending=False)

y = df['Survived']
x = df.drop(['Survived', 'PassengerId'], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)
pickle.dump(randomforest, open('titanic_model.sav', 'wb'))


# In[ ]:





# In[ ]:




