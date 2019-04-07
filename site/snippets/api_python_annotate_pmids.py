import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username='yourUsername', password='yourPassword')
params = {'project':'yourProject', 'owner':'yourUsername', 'idType':'PMID', 'ids':['23596191','29438695'], 'output':'ann.json'}
response = requests.post(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
