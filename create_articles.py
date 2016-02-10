import json
import requests
import random

howmany = 10 #enter how many posts you want created
section_id = 203133937
url = 'https://hainescorp.zendesk.com/api/v2/help_center/sections/' + str(section_id) + '/articles.json'
usr = 'nhaines@zendesk.com/token'
pwd = 'zg29l8wdec1FePJSuajpjZI9vF1h11lfy09LERcd'
headers = {'content-type': 'application/json'}

for x in range(0,howmany):
	#gets a random wikipedia
	response3 = requests.get('https://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exchars=500&format=json')
	data3 = response3.json()
	page = data3['query']['pages']
	title = page[page.keys()[0]]['title']
	details = page[page.keys()[0]]['extract']
	payload = {"article": {"title": title, "body": details}}
	payloaddata = json.dumps(payload)
	response4 = requests.post(url, data=payloaddata, auth=(usr, pwd), headers=headers)