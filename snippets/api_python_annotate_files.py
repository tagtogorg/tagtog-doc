import requests

tagtogAPIUrl = "https://www.tagtog.com/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username="yourUsername", password="yourPassword")
params = {"owner": "yourUsername", "project": "yourProject", "output": "ann.json"}
# you can append more files to the list in case you want to upload multiple files
files = [("files", open('files/text.txt'))]
response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
print(response.text)
