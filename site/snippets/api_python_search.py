import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username='yourUsername', password='yourPassword')
params = {'project':'yourProject', 'owner': 'yourUsername', 'search':'entity:GGP:P02649'}
response = requests.get(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
