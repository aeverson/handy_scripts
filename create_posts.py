import json
import requests
import random

howmany = 10 #enter how many posts you want created
url = 'https://your_subdomain.zendesk.com/api/v2/users.json'
usr = 'your@email.address'
pwd = 'yourpassword'
topic_id = 00000 #enter your topic ID here
headers = {'content-type': 'application/json'}
userarray = []

# Compiles a list of all user IDs
response1 = requests.get(url, auth=(usr, pwd))
data1 = response1.json()
userlist = data1['users']
for user in userlist:
	userarray.append(user['id'])
url = data1['next_page']
while url:
	response2 = requests.get(url, auth=(usr, pwd))
	data2 = response2.json()
	userlist = data2['users']
	for user in userlist:
		userarray.append(user['id'])
	url = data2['next_page']
numusers = len(userarray)

for x in range(0,howmany):
	#chooses random user to be the author
	enduser = userarray[random.randint(0, numusers-1)]

	#gets a random wikipedia
	response3 = requests.get('https://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exchars=500&format=json')
	data3 = response3.json()
	page = data3['query']['pages']
	title = page[page.keys()[0]]['title']
	details = page[page.keys()[0]]['extract']
	payload = {"post": {"title": title, "details": details, "author_id": enduser, "topic_id": topic_id}}
	payloaddata = json.dumps(payload)
	response4 = requests.post('https://z3nuglycats1.zendesk.com/api/v2/community/posts.json', data=payloaddata, auth=(usr, pwd), headers=headers)