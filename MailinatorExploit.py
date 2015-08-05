import string
import random
import requests
import json
import re
import time

RESERVATIONID = "" #5to6-character reservation ID
APITOKEN = "" # Mailinator API Token

def generateString():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))

while(True):
	currentEmail = generateString()
	timestamp = str(int(time.time())*1000)
	requestURL = "https://invites.oneplus.net/index.php?r=share/signup&success_jsonpCallback=success_jsonpCallback" + \
	             "&email={0}%40mailinator.com&koid={1}&_={2}".format(currentEmail, RESERVATIONID, timestamp)
	
	print("Sending invite to " + currentEmail + "@mailinator.com")
	res = requests.get(requestURL)

	mailinatorInbox = "https://api.mailinator.com/api/inbox?to=" + currentEmail + "&token=" + APITOKEN
	print("curling " + mailinatorInbox)

	time.sleep(5)
	response = requests.get(mailinatorInbox)
	while not response:
		time.sleep(2)
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

		time.sleep(1)

	if not emailID:
		continue

	mailinatorMessage = "https://api.mailinator.com/api/email?id=" + emailID + "&token=" + APITOKEN
	response = requests.get(mailinatorMessage)
	json_data = json.loads(response.text)
	content = json_data["data"]["parts"][0]["body"]

	m = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
	newURL = m.group(0).rstrip(".")
	print("Sending confirmation request to " + newURL)
	res = requests.get(m.group(0).rstrip("."))
	print("Referral sucessfully spoofed")
	print()
