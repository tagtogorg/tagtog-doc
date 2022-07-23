import requests

tagtogAPIUrl = "https://www.tagtog.com/-api/settings/v1/folders/add"

auth = requests.auth.HTTPBasicAuth(username='username', password='password')
params = {'project':'projectName', 'owner': 'ownername'}
payload = {'parentPath': 'pool', 'newFolderName':'myNewFolder'}
response = requests.post(tagtogAPIUrl, auth=auth, json=payload, params=params)
print(response.text)
