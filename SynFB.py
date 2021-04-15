# v. 1.0.0
import os
import logging
import time
import socket
import email
from email import utils
import fcntl
from Mail import Mail

DEST = '<DESTINATION-EMAIL>'
FROM = '<YOUR-EMAIL>'
PWD = '<YOUR-PASSWORD>'
SMTP = '<YOUR-SMTP-SERVER>'
PORT = 25

# Open File
myfile = open('SynFB.py')

# Lock the file
fcntl.flock(myfile, fcntl.LOCK_EX | fcntl.LOCK_NB)

# New Mail() instance
MM = Mail()

# Get hostname
host = socket.gethostname()

# Create log file
logging.basicConfig(filename="logs/log.txt", level=logging.INFO, format='%(asctime)s:%(message)s')
while 1 == 1:
    res = os.popen("netstat -ano | grep SYN_RECV |  awk {'print $4,$5'} | awk -F: {'print $1,$2'} | sort -k 3 | uniq -c | sort -k 1 | tail -1").read()
    if res != "":
        str = res.rstrip()
        logging.info(str)
        # Transform a string into an array
        arr = str.split()
        # If the first element of array it's >= 50 SynFB alert the admin mail configured at the top of this script.
        if int(arr[0]) >= 50:
                # Get timestamp with email format
                header = email.utils.formatdate(localtime=True)
                # Compile content of message
                msg = "%s - %s have %s SYN packets into netstat. Manually intervene." % (header, arr[3], arr[0])
                # Create message for send this one with send_mail
                messaggio = MM.crea_messaggio_mail(header, DEST, "SYN - %s", msg) % host
                # Send alert mail
                MM.send_mail(SMTP, PORT, FROM, PWD, DEST, messaggio)
                print ("Mail sended")
    else:
        continue
    time.sleep(40)
