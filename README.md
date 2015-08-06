# OnePlusTwo

## Mailinator Exploit (no longer working)

Context, Part 1:

https://medium.com/@JakeCooper/how-i-hacked-the-oneplus-reservation-system-120ea1a7ad82

Steps to use :

1. Fill in ```RESERVATIONID``` and ```APITOKEN``` at line 8-9
2. Download and install Requests (http://docs.python-requests.org/en/latest/)
3. Run! (`python MailinatorExploit.py`)

## Gmail Exploit (working as of 8.4.2015)
Context, Part 2:

https://medium.com/@JakeCooper/so-nice-i-did-it-twice-hacking-the-oneplus-reservation-system-again-2e8226c45f9a

### Method 1

1. Fill in ```gmailAddress``` and ```inviteToken``` at line 9-10
2. Run! (`python GmailExploit.py`)
3. Click links in your gmail inbox (or add a python script to automate this)

### Method 2
1. Run GmailExploit2.py
2. Enter your email WITH @gmail.com when prompted.
3. Enter your referral code (5-6 digits found on the end of your referral link)
3. Run EmailParser.py
4. Enter your email WITH @gmail.com.
5. Enter your password

## GuerrillaMail Exploit (working as of 8.4.2015)

Steps to use:

1. Fill in ```INVITE_TOKEN``` at line 9
2. (Optional) Change how long do you want to wait for the email to arrive ```EMAIL_CHECK_TIMEOUT``` at line 10
3. Download and install Requests (http://docs.python-requests.org/en/latest/)
4. Run! (`python GuerrillaMailExploit.py`)
##Additional Components

### gmailClicker - OnePlusTwo
Click on the confirmation link in a gmail message

Steps to use :

1. Insert your email adress and your password (line 38)
2. Install pip if it is not all done
3. Install request package -> pip install requests 
4. run it 

### EmailParser
Parses emails and curls the confirmation link automatically.

1. Run EmailParser.py
2. Enter your email
3. Enter your password.
