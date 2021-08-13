# Python sample code to automatically merge/adjudicate multiple documents using tagtog APIs
# The multiple documents come from the user's search query --> see `MY_SEARCH`

import requests
import os
import urllib.parse

# Set your tagtog credentials & project info
MY_USERNAME = os.environ.get('MY_TAGTOG_USERNAME','yourUsername')
MY_PASSWORD = os.environ.get('MY_TAGTOG_PASSWORD','yourPassword')
MY_PROJECT = os.environ.get('MY_TAGTOG_PROJECT','yourProjectName')

# the project owner could be a different user, but for simplicity we assume it's the same as your username
MY_PROJECT_OWNER = os.environ.get('MY_PROJECT_OWNER', MY_USERNAME)
TAGTOG_DOMAIN_CLOUD = "https://tagtog.net"
TAGTOG_DOMAIN = os.environ.get('TAGTOG_DOMAIN', TAGTOG_DOMAIN_CLOUD)
# When this is false, the SSL certification will not be verified (this is useful, for instance, for self-signed localhost tagtog instances)
VERIFY_SSL_CERT = (TAGTOG_DOMAIN == TAGTOG_DOMAIN_CLOUD)

# -----------------------------------------------------------------------------

# Set these parameters/variables as wishes for the Documents API for merging
MY_SEARCH = "*"
MERGING_STRATEGY = "union_v1"
SAVE_TO = "master"

# -----------------------------------------------------------------------------

tagtog_search_API = 'https://www.tagtog.net/-api/documents/v1'
auth = requests.auth.HTTPBasicAuth(username=MY_USERNAME, password=MY_PASSWORD)
search_param = {"owner": MY_PROJECT_OWNER, "project": MY_PROJECT, "search": MY_SEARCH }
tagtog_merge_API = 'https://www.tagtog.net/-api/documents/versions/v0/merge'
merge_param = {"owner": MY_PROJECT_OWNER, "project": MY_PROJECT, "strategy": MERGING_STRATEGY, "saveTo": SAVE_TO}

def url_encode(query):
    return urllib.parse.quote(query)

next_page = 0
while next_page != -1:
    search_param["output"] = "search"
    search_param["page"] = next_page
    response = requests.get(tagtog_search_API, params=search_param, auth=auth, verify=VERIFY_SSL_CERT)
    if response.text:
        json_dict = response.json()
        next_page = json_dict["pages"]["next"]
        for doc in json_dict["docs"]:
            merge_param["docid"] = doc["id"]
            DOC_ID = doc["id"]
            response_post = requests.post(tagtog_merge_API, params=merge_param, auth=auth, verify=VERIFY_SSL_CERT)
            assert response_post.status_code == 200
            DOC_URL = f"{TAGTOG_DOMAIN}/{MY_PROJECT_OWNER}/{MY_PROJECT}/-search/{url_encode(MY_SEARCH)}/{DOC_ID}"
            print(f"${DOC_ID} --> {DOC_URL}")
