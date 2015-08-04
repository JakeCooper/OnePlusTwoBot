import string
import random
import urllib.request
import requests
import json
import re
import time

def generateString():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))

while(True):
	currentEmail = generateString()
	requestURL = "https://invites.oneplus.net/index.php?r=share/signup&success_jsonpCallback=success_jsonpCallback&email={{0}}%40mailinator.com&koid={1}&_=1438595512634".format(currentEmail, "5-digitreservationID")
	
	print("Sending invite to " + currentEmail + "@mailinator.com")
	res = requests.get(requestURL)

	apiToken = "53009b6150c2482c95e1aca686546759"
	mailinatorInbox = "https://api.mailinator.com/api/inbox?to=" + currentEmail + "&token=" + apiToken
	print("curling " + mailinatorInbox)

	time.sleep(5)
	response = requests.get(mailinatorInbox)
	json_data = json.loads(response.text)

	emailID = None
	for i in range(0, 5):
		response = requests.get(mailinatorInbox)
		json_data = json.loads(response.text)

		for message in json_data["messages"]:
			if message["subject"] == "Confirm your email":
				emailID = message["id"]

		if emailID:
			break

		#print('sleep')
		time.sleep(1)

	if not emailID:
		continue

	mailinatorMessage = "https://api.mailinator.com/api/email?id=" + emailID + "&token=" + apiToken
	response = requests.get(mailinatorMessage)
	json_data = json.loads(response.text)
	print(json_data)
	content = json_data["data"]["parts"][0]["body"]

	m = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
	newURL = m.group(0).rstrip(".")
	print("Sending confirmation request to " + newURL)
	res = requests.get(m.group(0).rstrip("."))
	print("Referral sucessfully spoofed")
	print()
