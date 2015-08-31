import string
import random
import urllib
import urllib2
import time
import re
import smtplib

index = 0
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def id_generator(size, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))

def mail(Code):
	server.login("email1", "password")
	#Send the mail
	msg = ("\n OnePlus Bot found a invite! https://invites.oneplus.net/claim/{}".format(Code));
	server.sendmail("email1", "email2", msg)
	server.quit()
	print("Mail sent!")




while True:
	index += 1		
	s = "-";
	seq = (id_generator(2),id_generator(4),id_generator(4),id_generator(4));		
	Raw = s.join(seq);
	Code1 = ("GL" + Raw)
	Code2 = ("IN" + Raw)
	requestUrl1 = "https://invites.oneplus.net/claim/{0}".format(Code1)
	requestUrl2 = "https://invites.oneplus.net/claim/{0}".format(Code2)
	print(bcolors.OKBLUE + "Attempt {}" .format(index) + bcolors.ENDC)
	print("Url1: https://invites.oneplus.net/claim/" + Code1)
	req1 = urllib2.Request(requestUrl1)
	res1 = urllib2.urlopen(req1)
	website1 = res1.read()
	pattern = ">You entered an invalid invite</p>"
	m1 = re.search(pattern, website1)
	if m1:
		print(bcolors.FAIL + "Invalid Invite!" + bcolors.ENDC)
	else:
		print(bcolors.OKGREEN + "Invite found!" + bcolors.ENDC)
		
		with open("log.txt", "a") as text_file:
			text_file.write("Invite found! | https://invites.oneplus.net/claim/{}".format(Code1))
			text_file.write("\n")
		
		mail(Code1)
	
	print("Url2: https://invites.oneplus.net/claim/" + Code2)
	req2 = urllib2.Request(requestUrl2)
	res2 = urllib2.urlopen(req2)
	website2 = res2.read()
	m2 = re.search(pattern, website2)
	if m2:
		print(bcolors.FAIL + "Invalid Invite!" + bcolors.ENDC)
	else:
		print(bcolors.OKGREEN + "Invite found!" + bcolors.ENDC)
		
		with open("log.txt", "a") as text_file:
			text_file.write("Invite found! | https://invites.oneplus.net/claim/{}".format(Code2))
			text_file.write("\n")
		
		mail(Code2)
