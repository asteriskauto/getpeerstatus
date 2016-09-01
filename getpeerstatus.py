#!/usr/bin/python

import subprocess
import smtplib

proc = subprocess.Popen('asterisk -rx "sip show peers" |grep UNREACH | awk \'{print $1}\'', shell=True, stdout=subprocess.PIPE)
tmp = proc.stdout.read()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("YOUR_MAIL", "MAIL_PASSWORD")

msg = "Here are unreachable peers\r%s" %tmp
server.sendmail("YOUR_MAIL_FROM", "MAIL_TO", msg)
server.quit()
