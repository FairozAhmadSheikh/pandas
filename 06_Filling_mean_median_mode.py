# # replacing with mean median and mode 
import pandas as pd 

file_data=pd.read_csv('Titanic-Dataset.csv')

"""Mode """
# calculate mode of Cabin and fill na with the mode value 
m=file_data['Cabin'].mode()[0]
# fill using this mode 
file_data['Cabin']=file_data['Cabin'].fillna(m)
# display final output after filling with mode
print(file_data['Cabin'].info())

"""Mean"""
# calculte number of NaN values 
print(file_data.info())
# find mean
meann=file_data["Age"].mean()
# fill missing using mean 
file_data['Age']=file_data['Age'].fillna(meann)
# display final result 
print(file_data.info())


"""Median"""
# calculte number of NaN values 
print(file_data.info())
# find median
mediann=file_data['Age'].median()
# fill missing using median
file_data['Age']=file_data['Age'].fillna(mediann)
# display final result 
print(file_data.info())