# get data from a private gitHub reposory using the API

import requests
from config import api_keys
import json

target_url = 'https://api.github.com/repos/irenecelebrin/aprivateone'
api_key = api_keys['git_testkey']

response = requests.get(target_url, auth=('token', api_key))

response_json = response.json()

with open('4.2_git_response.json', 'w') as gr:
    json.dump(response_json, gr, indent=4)

