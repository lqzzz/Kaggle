# import csv
import numpy as np
import pandas as pd
# import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
def EDA():
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    quantitative = [f for f in train.columns if train.dtypes[f] != 'object']
    quantitative.remove('SalePrice')
    quantitative.remove('Id')
    qualitative = [f for f in train.columns if train.dtypes[f] == 'object']

    missing = train.isnull().sum()
    print(missing)
    print()
    missing = missing[missing > 0]
    print(missing)
    print()
    missing.sort_values(inplace=True)
    print(missing)
    print()
    # missing.plot.bar()
    # plt.show()

    # print(corr)
    # full_data = train,test
    # corr = train.drop('Id',axis = 1).corr().SalePrice
    # print(corr)
    # d = corr[corr<0.3].to_dict()
    # train = train.drop(corr[corr<0.3].to_dict().keys(),axis = 1)
    # print(train.info())
    
    # print(train.Street.iloc[:5])
    # print(train.iloc[0:4,0:10])
    # train,label = train[:,1:],train[:,0]
    # train = np.multiply(train,1.0/255)
    # l = np.zeros((42000,10))
    # for i in range(42000):
    #     l[i][int(label[i])] = 1
    # a = 0
    # for i in range(420):
    #     yield train[a:a + 100],l[a:a + 100]
    #     a += 100
EDA()