from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split            #Importing the necessary libraries
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
dataset=pd.read_csv('C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.1\Covid19data.csv') #Reading the covid-19 dataset using pandas
print(dataset.head())
dataset=dataset.replace([np.inf,-np.inf],np.nan).dropna(axis=0)  #Cleaning the dataset to increase the performance
