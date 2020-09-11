import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username='YourUsername', password='YourPassword')
params = {'project':'YourProjectName', 'owner': 'YourUsername', "output": "ann.json"}
#you can append more files to the list in case you want to upload multiple files
files = [("files", open('files/document.pdf', 'rb'))]
response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
print(response.text)
