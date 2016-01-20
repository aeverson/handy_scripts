import json
import requests
import ipsums
import random

for x in range(0, 7590):
# New ticket info
	subject = ipsums.subjects[random.randint(0, len(ipsums.subjects)-1)]
	body = ipsums.content[random.randint(0, len(ipsums.content)-1)]
	requestername = ipsums.requesters[random.randint(0, len(ipsums.requesters)-1)]
	requesteremail = ipsums.requesteremails[random.randint(0, len(ipsums.requesteremails)-1)]
# Package the data in a dictionary matching the expected JSON
	data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'requester' : {'name': requestername, 'email' : requesteremail}}}

# Encode the data to create a JSON payload
	payload = json.dumps(data)

# Set the request parameters
	url = 'https://z3ntrashpanda.zendesk.com/api/v2/tickets.json'
	user = 'bmanning@zendesk.com/token'
	pwd = 'L32j5yMIRFA2coSK2UlJPvdHYO3zViXm7M5j6DLS'
	headers = {'content-type': 'application/json'}

# Do the HTTP post request
	response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 201 (Created)
	#if response.status_code != 201:
    	#print('Status:', response.status_code, 'Problem with the request. Exiting.')
    	#exit()

# Report success
	print('Successfully created ticket # %d' % (x+1))