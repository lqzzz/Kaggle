import csv
import numpy as np
import pandas as pd
import tensorflow as tf
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns
def TrainData():
    tr = pd.read_csv('train.csv')
    t =  pd.read_csv('test.csv')
    data = [tr,t]
    for i in data:
        date = i.datetime.apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
        i['hour'] = date.apply(lambda x: x.hour)
        i['month'] = date.apply(lambda x: x.hour)
        i['day'] = date.apply(lambda x: x.hour)
        i['hour'] = date.apply(lambda x: x.hour)
        # i = i.drop('datetime',axis = 1)
    t = data[0]
    t['tc'] = abs(t['temp'] - t['atemp'])
    t = t[t['tc'] < 7]
    # d = t.loc[:,['humidity','count']].groupby('humidity',as_index = False).mean()
    # print(d.sort_values(by = 'humidity',ascending = False))
    # print(d.corr()['count'])
    fig,(ax1,ax2,ax3,ax4) = plt.subplots(ncols=4)
    fig.set_size_inches(12, 5)
    sns.regplot(x="temp", y="count", data=t,ax=ax1)
    sns.regplot(x="windspeed", y="count", data=t,ax=ax2)
    sns.regplot(x="humidity", y="count", data=t,ax=ax3)
    sns.regplot(x="hour", y="count", data=t,ax=ax3)
    plt.show()
    # t['ts'] = 0
    # t['ts'][(t.temp >= 10) & (t.temp < 21)] =1
    # t['ts'][(t.temp >= 21) & (t.temp < 35)] =2
    # t['ts'][t.temp >= 35] = 3

    # d = t.loc[:,['ts','count']].groupby('ts',as_index = False).mean()
    # print(d.sort_values(by = 'count',ascending = False))
    # print(d.corr()['count'])

    # d = t.loc[:,['temp','count']].groupby(['temp'],as_index = False).mean()
    
    # print(d.sort_values(by = 'count',ascending = False))
    # print(d.sort_values(by = 'temp',ascending = False))
    # print(d.corr()['count'])

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

    # d = t.loc[:,['hothour','count']].groupby('hothour',as_index = False).count().sort_values(by = 'count',ascending = True)
    # print(d)
    # print(d.corr()['count'])

    # d = t.loc[:,['hour','count']].groupby('hour',as_index = False).count().sort_values(by = 'count',ascending = True)
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

