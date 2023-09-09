#!/usr/bin/python3

import subprocess as s
import cgi
import smtplib


print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data1=form.getvalue("email")
data2=form.getvalue("info")



sender_email = "jidnyasabhavsar1182003@gmail.com"
sender_password = "gnxafwhhhijxtbnz"
recipient_email = data1
subject = "Test Email from Python"
body = data2

message = f"Subject: {subject}\n\n{body}"
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message)
        print("<pre><h2>")
        print("Email sent successfully.")
except Exception as e:
    print("<pre><h2>")
    print("Error sending email")
    print("</pre></h2>")