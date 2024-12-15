"""
Series is 1D Array or column of a table
Dataframe is like whole Table Like a 2d Array
"""

# Creating a Dataframe 

import pandas as pd 

workout={
    "calories":[100,200,300,400,500,600],
    "duration":[20,40,50,60,80,90]
}

df0=pd.DataFrame(workout)

# Specific Index && named index 
df1=pd.DataFrame(workout,index=["day0","day1","day2","day3","day4","day5",])
print(df1)


# locating Row using iloc() : Pandas uses the loc attribute to return one or more specified row 

# displaying as a series 
print(df0.loc[0])
print(df1.loc["day0"])

# displying as s dataframe
print(df0.loc[[0,1]])
print(df1.loc[["day0","day1"]])
