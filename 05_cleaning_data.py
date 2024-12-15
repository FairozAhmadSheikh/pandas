# cleaning data : It means fixing the bad data in our dataset , bad data could be : 
# empty cell, data in wrong format , duplicate and wrong data 


# Empty cell gives wrong result always, we will have the need to eliminate the row the contains bad data

# Loading and reading original Data Frame 
import pandas as pd 

data=pd.read_csv('Titanic-Dataset.csv')
print(data.info())

# dropna()  method is used to drop not a number value in a column 
"""Never clean original dataset , make a copy and clean that one """
data2=pd.read_csv('Titanic-Dataset.csv')
new_data=data2.dropna()

print(new_data)


# Way to clean orignal dataset 
data=pd.read_csv('Titanic-Dataset.csv')
data=data.dropna(inplace=True)
print(data)


# Fillna() used to fill not a number values with some values 

org_data=pd.read_csv('Titanic-Dataset.csv')
org_data.fillna(130,inplace=True)
print(org_data)