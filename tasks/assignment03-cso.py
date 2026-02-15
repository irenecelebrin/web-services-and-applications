# task 3: Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
# date: 15-02-2026
# author: irene celebrin 

import requests
import json 

# navigate the cso website and find the API url 
url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en'

# get data from the API 
response = requests.get(url)
# use json_dump to save to a json file 
with open('cso.json','w') as json_file:
    json.dump(response.json(), json_file)



