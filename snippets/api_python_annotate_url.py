import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username='yourUsername', password='yourPassword')
params = {"owner": "yourUsername", "project": "yourProject", 'output':'weburl', 'url':'https://en.wikipedia.org/wiki/Autonomous_cruise_control_system'}
response = requests.post(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
