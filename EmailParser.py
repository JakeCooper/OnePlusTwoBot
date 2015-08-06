import sys
import imaplib
import getpass
import email.header
import re
import datetime
import json
import email
import requests
import time

f = open("confirmations.txt", "w")

EMAIL = input("Email : ")
PASSWORD = input("Password : ")
def processMailbox(M):
	M.select()
	typ, data = M.search(None, 'SUBJECT "Confirm your email"', '(BODY "OnePlus")')
	for num in data[0].split():
		typ, data = M.fetch(num, '(RFC822)')
		msg = email.message_from_string(data[0][1].decode('utf-8'))
		if msg.is_multipart():
			for payload in msg.get_payload():
				manipulatePayload(payload)
				break

		else:
			manipulatePayload(msg) 
				

def manipulatePayload(payload):
	m = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.', str(payload.get_payload(None, True)))
	newURL = m.group(0).rstrip(".")
	f.write(newURL + "\n")
	print("Sending confirmation request to " + newURL)
	res = requests.get(m.group(0).rstrip("."))
	if res.status_code == 200:
	 	print("Referral sucessfully spoofed")
	else :
	 	print("Hamsters are dead")
	print()
	
	return


M = imaplib.IMAP4_SSL('imap.gmail.com')

try :
	M.login(input("Email : "), input("password : "))
except imaplib.IMAP4.error:
	print("LOGIN FAILED")

rv, mailboxes = M.list()
if rv == 'OK' :
	print("Selecting Mailbox Inbox")
	processMailbox(M)
	M.close()
M.logout()
f.close()	
