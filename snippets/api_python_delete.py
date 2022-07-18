import requests

tagtogAPIUrl = "https://www.tagtog.com/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username="yourUsername", password="yourPassword")
params = {"owner": "yourUsername", "project": "yourProject", 'search':'entity:gene'}
response = requests.delete(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
