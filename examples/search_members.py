import requests
import json

project_name = 'Best_Public_Project'
project_owner = 'demo'
tagtog_projects_API = 'https://www.tagtog.net/-api/projects/v1/my_projects'
tagtog_search_API = 'http://www.tagtog.net/-api/documents/v1'
auth = requests.auth.HTTPBasicAuth(username='yourUsername', password='yourPassword')

def export_project():
    response = requests.get(tagtog_projects_API, auth=auth)
    projects = json.loads(response.text)
    filtered_project = 
    list(filter(lambda d: d['name'] == project_name and d['owner'] == project_owner,projects))
    return dict(filtered_project[0])

def get_members(project):
    members_list = list(map(lambda x: x['username'] if x['role'] != 'reader' else None, project['members']))
    curated_members_list = [x for x in members_list if x is not None]
    return curated_members_list

def get_number_documents_completed(member):
    search = 'members_anncomplete:' + member
    params = {'project':project_name,'owner':project_owner,'search':search}
    response = requests.get(tagtog_search_API,params=params,auth=auth)
    result = json.loads(response.text)
    return len(result['docs'])

def get_confirmed_documents():
    params = {'project':project_name,'owner':project_owner,'search':'members_anncomplete:*'}
    response = requests.get(tagtog_search_API,params=params,auth=auth)
    result = json.loads(response.text)
    return result['docs']

if __name__ == '__main__':
    project = export_project()    
    members = get_members(project)
    with open('members_anncomplete.txt','w') as f:
        for member in members:
            num_docs_anncompleted = get_number_documents_completed(member)
            f.write(member + ': ' + str(num_docs_anncompleted)+ "\n")
            
    documents = get_confirmed_documents() 
    with open('documents_completed.txt','w') as f:
        for doc in documents:
            f.write(doc['id'] + "\n")

