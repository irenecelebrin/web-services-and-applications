# assignment 04 - access and modify private github data using the github api
# author: irene celebrin
# date: 2026-02-22

# import modules 
import requests
from config import api_keys 
import base64

# --- CONFIG ---
# get github token and repo info 
TOKEN = api_keys["github_token"]  
OWNER = "irenecelebrin"
REPO = "aprivateone"
PATH = "code.py"

# --- HEADERS ---
# set authorization token and content negotioation (json, v3 of github api)
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# --- 1. GET FILE CONTENT ---
# path to file 
url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}"

# get content and riase error if request failed
response = requests.get(url, headers=headers)
response.raise_for_status()

# convert to json, get sha and content (base64 encoded)
file_data = response.json()
file_sha = file_data["sha"]
content_encoded = file_data["content"]

# Decode base64 content
content_decoded = base64.b64decode(content_encoded).decode("utf-8")

# --- 2. MODIFY CONTENT ---
#modify content and re-encode before committing 
updated_content = content_decoded.replace("andrew", "irene")
updated_content_encoded = base64.b64encode(updated_content.encode("utf-8")).decode("utf-8")

# --- 3. UPDATE FILE ---
update_payload = {
    "message": "Replace 'andrew' with 'irene'",
    "content": updated_content_encoded,
    "sha": file_sha
}

# send update request and raise error if failed
update_response = requests.put(url, headers=headers, json=update_payload)
update_response.raise_for_status()

print("File successfully updated!")
