# viewing the data : one of the most used method for ma quick view of the dataframes is head() and tail() method
# These both methods return specific number of rows 

import pandas as pd 

data=pd.read_json('iris.json')
# to display all rows on terminal .to_string()
# print(data.to_string())

# to display first 5 rows we can use .head()
print(data.head())

print()

# to display last 5 rows we can use .tail()
print(data.tail())


# to display specific number of rows using head() and tail() method pass number of rows as a parameter

print(data.head(10))
print(data.tail(7))


# Information about the data in the dataframe can be obtained by : info()

print(data.info())