import csv
import numpy as np
import pandas as pd

def NextTrainData():
    a = 0
    data = pd.read_csv('train.csv').values
    for i in range(42):
        train,label = None,None
        if(i != 41):
           train,label = data[a:a+1024,1:],data[a:a+1024,1]
        else:
           train,label = data[a:,1:],data[a:,1]
        a += 1024
        train[train>0] = 1
        l = np.zeros((label.shape[0],9))
        label = np.column_stack((label,l))
        for i in range(label.shape[0]):
            index = label[i][0] 
            label[i][0] = 0
            label[i][int(index)] = 1
        yield train,label     
        
def NextTestData():
    data = pd.read_csv('test.csv').values
    a = 0
    print(data.shape)
    for i in range(28):
        test_data = None
        if(i != 27):
           test_data = data[a:a+1024]
        else:
            test_data = data[a:]
        a += 1024
        test_data[test_data > 0] = 1
        yield test_data 
        
def NextTestResult():
    data = pd.read_csv('sample_submission.csv').values
    a = 0
    for i in range(28):
        test_result = None
        if(i != 27):
           test_result = data[a:a+1024,1:]
           print(data[a:a+1024,0:])
        else:
           test_result = data[a:,1:]
        a += 1024
        print(test_result)
        l = np.zeros((test_result.shape[0],9))
        test_result = np.column_stack((test_result,l))
        for i in range(test_result.shape[0]):
            index = test_result[i][0] 
            test_result[i][0] = 0
            test_result[i][int(index)] = 1
        yield test_result
s_data = pd.read_csv('gender_age_train.csv')
print(s_data.head())