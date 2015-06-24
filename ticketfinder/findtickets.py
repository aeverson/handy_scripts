import requests
import agentlist

# Set the request parameters
subdomain = ''
url = 'https://'+subdomain+'.zendesk.com/api/v2/tickets.json'
user = ''
pwd = ''
triggerID = 47269281

issues_list = []
def checkAudits(id):
	response1 = requests.get('https://'+subdomain+'.zendesk.com/api/v2/tickets/' + str(id) + '/audits.json', auth=(user,pwd))
	data1 = response1.json()
	audits_list = data1['audits']
	for audit in audits_list:
	    publiccommentbyagent = False
	    triggerfired = False
	    events_list = audit['events']
	    for event in events_list:
	        if (event['type'] == 'Comment'):
	            if event['author_id'] in agentlist.agents:
	                if event['public'] == True:
	                    publiccommentbyagent = True
	        if event['type'] == 'Notification':
	        	if event['subject'] != "{{dc.csat_mail_subject}}":
		            if event['via']['source']['from']['id'] == triggerID:
		                triggerfired = True;
	    if (publiccommentbyagent == True) & (triggerfired == False):
	        print("Houston, we have a problem on Ticket #" + str(id) + ' update ID #' + str(event['id']))
	        issues_list.append(str(id))


# pagination

while url:
	response = requests.get(url, auth=(user, pwd))
	data = response.json()
	ticket_list = data['tickets']
	for ticket in ticket_list:
		if ("quick_solve" in ticket['tags']) & (ticket['via']['channel'] != "twitter"):
			checkAudits(ticket['id'])
		print(ticket['id'])
	url = data['next_page']

print("Issues list:")
print(issues_list)