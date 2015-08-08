import imaplib
import string
import urllib2
import time
import email
import re
import requests

def processMailbox(M):
    M.select()
    typ, data = M.search(None, 'UnSeen', 'SUBJECT', '"Confirm your email"', 'FROM', 'invites@oneplus.net')
    mails = data[0].split()
    print "There are %i unseen invites!" % len(mails)
    for num in mails:
        typ, data = M.fetch(num, '(RFC822)')
        msg = email.message_from_string(data[0][1].decode('utf-8'))
        if msg.is_multipart():
            for payload in msg.get_payload():
                manipulatePayload(payload)
                break
        else:
            manipulatePayload(msg)

def manipulatePayload(payload):
    m=re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\.', str(payload.get_payload(None,True)))
    newURL = m.group(0).rstrip(".")
    print("Sending confirmation request to " + newURL)
    while True:
        try:
            res = requests.get(m.group(0).rstrip("."), timeout=1)
            if res.status_code == 200:
                print("Referral successfully spoofed")
            else :
                print("Request failed. "+str(res.status_code))
            time.sleep(5)
            return
        except:
            continue

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


