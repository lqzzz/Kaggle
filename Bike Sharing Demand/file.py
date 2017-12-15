import csv
import numpy as np
import pandas as pd
import tensorflow as tf
import datetime as dt
def TrainData():
    tr = pd.read_csv('train.csv')
    t =  pd.read_csv('test.csv')
    data = [tr,t]
    for i in data:
        date = i.datetime.apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
        i['hour'] = date.apply(lambda x: x.hour)
        # i = i.drop('datetime',axis = 1)
    t = data[0]
    t['t'] = 0.4 * t['temp'] + 0.6 * t['atemp'] 
    t['tc'] = abs(t['temp'] - t['atemp'])
    t['c'] = 1
    d = t.loc[:,['tc','c']].groupby('tc',as_index = False).sum()
    print(d)
    # d = t.loc[:,['t','count']].groupby('t',as_index = False).sum()
    # d = t.loc[:,['temp','atemp','count']].groupby(['temp','atemp'],as_index = False).mean()
    # print(d.sort_values(by = 'count',ascending = False).corr()['count'])
    # print(d.sort_values(by = 'count',ascending = False))
    # print(d.corr()['count'])
    # print(d)

    # t['hotseason'] = 1
    # t['hotseason'][t['season'] == 0] = 0

    # t['hothour'] = 0

    # t['hothour'][t['hour'] == 0] = 1
    # t['hothour'][t['hour'] == 9] = 1
    # t['hothour'][t['hour'] == 10] = 1
    # t['hothour'][t['hour'] == 20] = 1
    # t['hothour'][t['hour'] == 22] = 1
    # t['hothour'][t['hour'] == 23] = 1

    # t['hothour'][t['hour'] == 7] = 2
    # t['hothour'][t['hour'] == 11] = 2
    # t['hothour'][t['hour'] == 13] = 2
    # t['hothour'][t['hour'] == 14] = 2
    # t['hothour'][t['hour'] == 15] = 2
    # t['hothour'][t['hour'] == 21] = 2


    # t['hothour'][t['hour'] == 8] = 3
    # t['hothour'][t['hour'] == 12] = 3
    # t['hothour'][t['hour'] == 16] = 3
    # t['hothour'][t['hour'] == 17] = 3
    # t['hothour'][t['hour'] == 18] = 3
    # t['hothour'][t['hour'] == 19] = 3

    # d = t.loc[:,['hothour','count']].groupby('hothour',as_index = False).max().sort_values(by = 'count',ascending = True)
    # print(d)
    # print(d.corr()['count'])

    # d = t.loc[:,['hour','count']].groupby('hour',as_index = False).max().sort_values(by = 'count',ascending = True)
    # print(t['hothour'])
    # print(t.hothour)
    # print(d,'\n',d.corr()['count'])
    # print(d.groupby('hour',axis = 0).sum().sort_values(by = 'count',ascending = True))
    # t = t.drop(['datetime','casual','registered'],axis = 1)
    # lable = t['count']
    # print(t['hour'])
    # t['CH'] = pd.cut(t['hour'], 5)
    # print(t['CH'])
    # a = 
    # for i in range(54):
    #     yield data[0][a:a+200],lable[a:a+200]
    #     a += 200
TrainData()

