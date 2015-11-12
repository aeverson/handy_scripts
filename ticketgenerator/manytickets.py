import json
import requests
import ipsums
import random

for x in range(0, 6):
# New ticket info
	subject = ipsums.subjects[random.randint(0, len(ipsums.subjects)-1)]
	body = ipsums.content[random.randint(0, len(ipsums.content)-1)]
	requestername = ''
	requesteremail = ''
# Package the data in a dictionary matching the expected JSON
	data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'requester' : {'name': requestername, 'email' : requesteremail}}}

# Encode the data to create a JSON payload
	payload = json.dumps(data)

# Set the request parameters
	url = 'https://subdomain.zendesk.com/api/v2/tickets.json'
	user = ''
	pwd = ''
	headers = {'content-type': 'application/json'}

# Do the HTTP post request
	response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 201 (Created)
	#if response.status_code != 201:
    	#print('Status:', response.status_code, 'Problem with the request. Exiting.')
    	#exit()

# Report success
	print('Successfully created ticket # %d' % (x+1))