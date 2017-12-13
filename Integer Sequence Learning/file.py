import numpy as np
import pandas as pd

def TrainData():
    data = pd.read_csv('train.csv')
    print(data.shape)
    data['Sequence'] = data['Sequence'].map(lambda x: x.split(','))
    print(data.Sequence[0])
def TestData():
    data = pd.read_csv('test.csv')
    print(data.head())
# TestData()
TrainData()
# TrainData()