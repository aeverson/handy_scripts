import requests

# Set the request parameters
subdomain = ''
url = 'https://'+subdomain+'.zendesk.com/api/v2/users.json'
user1 = ''
pwd = ''

agent_array = []
while url:
	# Do the HTTP get request
	print(url)
	response = requests.get(url, auth=(user1, pwd))

	# Check for HTTP codes other than 200
	if response.status_code != 200: 
	    print('Status:', response.status_code, 'Problem with the request. Exiting.')
	    exit()

	# Decode the JSON response into a dictionary and use the data
	data = response.json()

	# add every agent's user ID to an array
	user_list = data['users']
	for user in user_list:
		if user['role'] != 'end-user':
			agent_array.append(user['id'])
	url=data['next_page']
# print the array
print(agent_array)