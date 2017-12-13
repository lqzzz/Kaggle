import numpy as np
import pandas as pd
import tensorflow as tf

def TrainData():
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    test.loc[test.Age.isnull(),'Age'] = 30.0 
    train.loc[train.Age.isnull(),'Age'] = 29.0
    train.Cabin = train.Cabin.isnull().apply(lambda)
    # print(train[train['Age'].isnull()].Age.values)
    # print(train['Age'])

    # print(train[train['Age'].notnull()][['Survived','Age']])
    # print(train.info())
TrainData()

