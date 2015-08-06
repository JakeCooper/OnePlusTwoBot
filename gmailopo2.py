import imaplib
import string
import urllib2
import time
import email
import re
import requests

def processMailbox(M):
    M.select()
    typ, data = M.search(None, 'SUBJECT', '"Confirm your email"')
    for num in data[0].split():
        typ, data = M.fetch(num, '(RFC822)')
        msg = email.message_from_string(data[0][1].decode('utf-8'))
        if msg.is_multipart():
            for payload in msg.get_payload():
                manipulatePayload(payload)
                break
        else:
            manipulatePayload(msg.get_payload())

def manipulatePayload(payload):
    m=re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.', str(payload.get_payload(None,True)))
    newURL = m.group(0).rstrip(".")
    print("Sending confirmation request to " + newURL)
    res = requests.get(m.group(0).rstrip("."))
    if res.status_code == 200:
        print("Referal successfully spoofed")
    else :
        print("Hamsters are dead")
    print()
    time.sleep(5)
    return

M= imaplib.IMAP4_SSL('imap.gmail.com')

try:
    M.login('emailadress@gmail.com', "password")
except imaplib.IMAP4.error:
    print("LOGIN FAILED")

rv, mailboxes = M.list()
if rv == 'OK' :
    print("Selecting Mailbox Inbox")
    processMailbox(M)
    M.close()
M.logout()


