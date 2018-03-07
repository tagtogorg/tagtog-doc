import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username='yourUsername', password='yourPassword')
params = {'project':'yourProject', 'owner': 'yourUsername', 'ids':'aVTjgPL0x5m_xgJr3qcpfXcSoY_q-text', 'output':'ann.json'}
response = requests.get(tagtogAPIUrl, params=params, auth=auth)
print(response.text)
