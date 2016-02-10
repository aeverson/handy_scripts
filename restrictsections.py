import requests
import json

targettag = '' #the org tag we're looking for
sectionid = '' #the section ID we want to restrict, note:must be a string
user = '' #agent email, may use /token
pwd = '' #agent password or API token
subdomain = 'https://subdomain.zendesk.com/' #account URL
taggedorgs = []

#get organizations
response = requests.get(subdomain+'api/v2/organizations.json', auth=(user, pwd))
data = response.json()
org_list = data['organizations']

#go through orgs and add to taggedorg list if it has the target tag
for org in org_list:
	if targettag in org['tags']:
		taggedorgs.append(org['id'])

#paginate through all org pages
while data["next_page"]:
	response = requests.get(data["next_page"], auth=(user, pwd))
	data = response.json()
	org_list = data['organizations']

	for org in org_list:
		if targettag in org['tags']:
			taggedorgs.append(org['id'])

#post the tagged org list to the access_policy endpoint to restrict the section
headers = {'content-type': 'application/json'}
data1 = {"access_policy":{"restricted_to_organization_ids":taggedorgs}}
payload = json.dumps(data1)
response1 = requests.put(subdomain+'/api/v2/help_center/sections/'+sectionid+'/access_policy.json', data=payload, auth=(user, pwd), headers=headers)

#print error if there is one
if response.status_code != 200: 
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
else:
	print('Complete')


