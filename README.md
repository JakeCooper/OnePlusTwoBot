# OnePlusTwo

## Mailinator Exploit (no longer working)

Context, Part 1:

https://medium.com/@JakeCooper/how-i-hacked-the-oneplus-reservation-system-120ea1a7ad82

Steps to use :

1. Fill in ```RESERVATIONID``` and ```APITOKEN``` at line 8-9
1. Download and install Requests (http://docs.python-requests.org/en/latest/)
1. Run! (`python MailinatorExploit.py`)

## Gmail Exploit (working as of 8.4.2015)

Context, Part 2:

https://medium.com/@JakeCooper/so-nice-i-did-it-twice-hacking-the-oneplus-reservation-system-again-2e8226c45f9a

Steps to use :

1. Fill in ```gmailAddress``` and ```inviteToken``` at line 9-10
1. Run! (`python GmailExploit.py`)
1. Click links in your gmail inbox (or add a python script to automate this)

## GuerrillaMail Exploit (working as of 8.4.2015)

Steps to use:

1. Fill in ```INVITE_TOKEN``` at line 9
1. Download and install Requests (http://docs.python-requests.org/en/latest/)
1. Run! (`python GuerrillaMailExploit.py`)
