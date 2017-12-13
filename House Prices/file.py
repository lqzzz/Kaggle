# import csv
import numpy as np
import pandas as pd
# import tensorflow as tf

def TrainData():
    data = pd.read_csv('train.csv')
    # print(data.info())
    # print(data.MSZoning)
    # print(data.describe().iloc[0:5,0:5])
    print(data.drop('Id',axis = 1).corr().SalePrice)
    print(data.Street.iloc[:5])
    # print(data.iloc[0:4,0:10])
    # train,label = data[:,1:],data[:,0]
    # train = np.multiply(train,1.0/255)
    # l = np.zeros((42000,10))
    # for i in range(42000):
    #     l[i][int(label[i])] = 1
    # a = 0
    # for i in range(420):
    #     yield train[a:a + 100],l[a:a + 100]
    #     a += 100
TrainData()