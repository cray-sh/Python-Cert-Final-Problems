"""
Author: Cray-sh
Date: 2023.01.28

This is problem 3 for course 6 of the python cert
I will try to keep the same format, several blocks that include cases/scenerios that slowly
ramp up in difficulty/complexity.

Problem Description:


"""
#shebang will be below here
#!/usr/bin/env python3

#%% Block 1: simple example

#importing

from email.message import EmailMessage
import os.path
import mimetypes

message = EmailMessage()

#setting email headers

sender = "me@example.com"
recipient = "you@example.com"
subject = "Example Email Subject"


message["From"] = sender
message["To"] = recipient
message["Subject"] = subject

#setting body of email

body = '''This is a body
            of an email that could be as
            long as you want it to be'''
            
message.set_content(body)

#Below will be setting up to attach a file

attach_path = ""

#Below sets up a way for us to get the mimetype and subtype that will need to be set
#before we can send the message

attach_filename = os.path.basename(attach_path)

#I'm not sure why they recommend/use the underscore below when setting a variable

mime_type, _ = mimetypes.guess_type(attach_path)

#this is a little trick to redefine them quickly

mime_type,mime_subtype = mime_type.split('/',1)

#now we can finally attach the picture/file to the message
#notice we needed the path to open the file, then
#to attach we needed: read the file, maintype(which is mime_type), subtype(which is mime_subtype,
#and the filename

with open(attach_path, 'rb') as ap:
    
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=attach_filename)

#Adding a file will add a HUGE string when printing message, shorten it in oneway or another
print(message)




















