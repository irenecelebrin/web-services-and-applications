# use API to convert HTML to PDF 

import requests
from config import api_keys
import urllib.parse

# API documntion: https://html2pdf.app/documentation/

# set url and api key 
target_url = 'https://andrewbeatty1.pythonanywhere.com/bookviewer.html'
api_key = api_keys['html2pdf']
api_url = 'https://api.html2pdf.app/v1/generate'

# set paramters 
params = {
    'url': target_url,
    'apiKey': api_key
}
parsed_params = urllib.parse.urlencode(params)
requesturl = api_url + '?' + parsed_params

# send request 
response = requests.get(requesturl)

print(response.status_code)

with open('4.2_html2pdf.pdf', 'wb') as f:
    f.write(response.content)

