import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username="yourUsername", password="yourPassword")
params = {"owner": "yourUsername", "project": "yourProject", "output": "ann.json"}
payload = {'text': 'Antibody-dependent cellular cytotoxicity (ADCC), a key effector function for the clinical effectiveness of monoclonal antibodies, is triggered by the engagement of the antibody Fc domain with the Fcγ receptors expressed by innate immune cells such as natural killer (NK) cells and macrophages.'}
response = requests.post(tagtogAPIUrl, params=params, auth=auth, data=payload)
print(response.text)
