# lab 2
# irene celebrin

import csv 
import requests 
import json

filename = "./people.csv"

# import data from csv, all types are strings 
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    
    rowcount = 0
    total = 0 
    for row in reader:
        if rowcount == 0:
            pass
        else:
            total += int(row[1])
        rowcount += 1
        
    #print(f'average is {total/(rowcount-1)}')


# import data from csv, usign quoting to recognise numbers as ints  
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter = ',', quoting = csv.QUOTE_NONNUMERIC)
    
    rowcount = 0
    total = 0 
    for row in reader:
        if rowcount == 0:
            pass
        else:
            total += row[1]
        rowcount += 1
        
    #print(f'average is {total/(rowcount-1)}')

# import using dictReader 

with open(filename, 'rt') as fp:
    reader = csv.DictReader(fp, delimiter = ',', quoting = csv.QUOTE_NONNUMERIC)
    
    rowcount = 0
    total = 0 
    for row in reader:
        total += row['age']
        rowcount += 1
        
    #print(f'average is {total/rowcount}')

# read json from internet 

url = "https://www.gov.uk/bank-holidays.json"
# convert json to python dict
response = requests.get(url)
data = response.json()

# print(data)

norther_ireland = data['northern-ireland']['events'][0]

print(norther_ireland)