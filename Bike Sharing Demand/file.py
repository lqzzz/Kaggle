import csv
import numpy as np
import pandas as pd
import tensorflow as tf
import datetime as dt
def TrainData():
    tr = pd.read_csv('train.csv')
    t =  pd.read_csv('test.csv')
    data = [tr,t]
    
    for i in range(2):
        date = data[i].datetime.apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
        data[i]['month'] = date.apply(lambda x: x.month)
        data[i]['day']= date.apply(lambda x: x.day)
        data[i]['hour'] = date.apply(lambda x: x.hour)
        data[i] = data[i].drop('datetime',axis = 1)
    for i in data:
        print(i.info())
    lable = data[0]['count']
    data[0] = data[0].drop('count',axis = 1)
    # print(data.describe())
    # print(data.corr()['count'])
    # print(data.season)
    # print(data.head())
    a = 0
    for i in range(54):
        yield data[0][a:a+200],lable[a:a+200]
        a += 200
    
TrainData()

