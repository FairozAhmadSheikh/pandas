"""Pandas is a python library used for working with datasets
it has fucnctions for analyzing and cleaning ,explorng and manipulating data
PANDAS === PYTHON DATA ANALYSIS"""

import pandas as pd 
 
list1=[1,2,3,4,5,6,7,8,9]

# Craeting a series 

s1=pd.Series(list1)
print(s1)


# labeling can be used to access a specified value 
print(s1[3])

# Creating custmm labels 

s2=pd.Series([1,2,3],index=["a","b","c"])
# display all
print(s2)

# display custom label

print(s2["b"])

# creating series from dictionary

cal={"day1":100,"day2":200,"day3":400}

sd=pd.Series(cal)
print(sd)

# creating series using day1 and day2

sn=pd.Series(cal,index=["day1","day2"])
print(sn)