import requests

tagtogAPIUrl = "{{ page.api_document_url }}"

auth = requests.auth.HTTPBasicAuth(username='{{ page.api_username }}', password='{{ page.api_pwd }}')
params = {'project':'{{ page.api_project }}', 'owner': '{{ page.api_username }}', 'output':'ann.json'}
#you can append more files to the list in case you want to upload multiple files
files = [('file', open('files/document.pdf'))]
response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
print(response.text)
