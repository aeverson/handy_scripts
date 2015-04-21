import requests
import sys
import json

# If the user ID and tag(s) are included in the arguments:
if len(sys.argv) > 2:

	# First arg is the user id
	id = sys.argv[1]

	# The rest of the args are the new tags
	newtaglist = []
	for x in range(2, len(sys.argv)):
		newtaglist.append(sys.argv[x])

elif len(sys.argv) == 2:
	id = sys.argv[1]
	newtaglist = raw_input("Enter the tag(s) you'd like to add (separated by spaces): ")
	newtaglist = newtaglist.split(" ")

elif len(sys.argv) == 1:
	id = str(raw_input("Enter the user ID: "))
	newtaglist = raw_input("Enter the tag(s) you'd like to add (separated by spaces): ")
	newtaglist = newtaglist.split(" ")

# Set the request parameters
url = 'https://subdomain.zendesk.com/api/v2/users/' + id + '.json'
user = ''
pwd = ''

# Do the HTTP get request
response1 = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response1.status_code != 200: 
    print('Status:' + str(response1.status_code) + ' Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data1 = response1.json()

# Add new tags to old tags
tag_list = data1['user']['tags']
for x in range(0, len(newtaglist)):
	tag_list.append(newtaglist[x])

# Package the data in a dictionary matching the expected JSON
data2 = { 'user': { 'tags': tag_list } }

# Encode the data to create a JSON payload
payload = json.dumps(data2)

# Do the HTTP put request
response2 = requests.put(url, data=payload, auth=(user, pwd), headers={'content-type': 'application/json'})

# Check for HTTP codes other than 200
if response2.status_code != 200:
    print('Status:', response2.status_code, 'Problem with the request. Exiting.')
    exit()

# Report success
print('Successfully added tag(s) to user #{}'.format(id))
