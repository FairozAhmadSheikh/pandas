import pandas as pd 

# Loading a csv file (comma seperated values)
file=pd.read_csv('Titanic-Dataset.csv')
# Printing file as df 
print(file)

# maximum row handling capacity of your machine

print(pd.options.display.max_rows,": Rows")

"""
Bypassing the limit of maximum rows  (Can be dangerous ⚡⚡) 
#pd.options.display.max_rows=9999
print(pd.options.display.max_rows,": Rows")
"""

# Read JSON FILE 
 
json_data=pd.read_json("iris.json")
print(json_data)  # Use tostring() to display whole dataset on terminal



# Dicionaray as a json file : when we have dictionaray in our code not as a file then we handle it as below

database={
    "user_id":{"0":"ABDUL BARI","1":"MOHSIN JAMEEL","2":"EESA_YOUSUF","3":"SAMEER","4":"HUSSAIN"},
    "marks":{"0":100,"1":30,"2":101,"3":33,"4":21},
    "Grade":{"0":"A","1":"B","2":"C","3":"D","4":"E"},
}

JSON_HOLDER=pd.DataFrame(database)
print(JSON_HOLDER)

print(JSON_HOLDER.iloc[2])