import json
import requests

# # Set the request parameters
subreddit = "finishing"
url = 'https://z3nzdsupport.zendesk.com/api/v2/tickets.json'
user = ''
pwd = ''
headers = {'content-type': 'application/json'}

# Get Reddit post
# Need to figure out how to get many posts and get a new one each time
content = requests.get('https://www.reddit.com/r/'+subreddit+'.json?limit=100')


if content.status_code != 200:
    print('Status:', content.status_code, 'Problem with the request. Exiting.')
    exit()

for x in range (0,99):
	if content.json()['data']['children'][x]['data']['selftext'] != '':
		title = content.json()['data']['children'][x]['data']['title']
		comment = content.json()['data']['children'][x]['data']['selftext']
		requestername = content.json()['data']['children'][x]['data']['author']
		requesteremail = content.json()['data']['children'][x]['data']['author'] + "@example.com"
		newticket = {"ticket": {"subject": title, "comment": comment, "requester":{"name": requestername, "email":requesteremail} }}
		payload = json.dumps(newticket)
		
		# # Do the HTTP put request
		response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)

		# # Check for HTTP codes other than 200
		if response.status_code != 201:
		    print('Status:', response.status_code, 'Problem with the request. Exiting.')
		    exit()