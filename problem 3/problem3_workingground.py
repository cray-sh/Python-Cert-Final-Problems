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

#%% Block 1: simple example - Sending a message

#importing

from email.message import EmailMessage
import os.path
import mimetypes
import getpass
import smtplib

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

attach_path = "C:\\Users\\ADP55\\Desktop\\testfolder\\gobble.jpg"

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

#Below are the info to set for the smtp site for outgoing messages, and a password asker to use later

smtp_site = input("what is the smtp address to use")

mail_pass = getpass.getpass("password? ")

#now that we have that info we can open a server using the smtp site, setting debug to 1 is on to see
#debug info

mail_server = smtplib.SMTP_SSL(smtp_site)
mail_server.set_debuglevel(1)

#authenticates the connection using the username (email of sender) and password
#it will ouput a tuple that will have a status code and message

#Note!!! If this autentication fails it will raise a SMTPAuthenticationError exception, you'll need
#to figure out a way to handle those!

mail_server.login(sender, mail_pass)

#finally the message with attachments is sent via the smtp server and then closed upon completion

mail_server.send_message(message)
mail_server.quit()


#%% Block 2 - Generate PDF Simple Example

#I'm going to group all of the import lines together here
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image   #these are the flowables
from reportlab.lib.styles import getSampleStyleSheet                                #this is used for style references for text
from reportlab.lib import colors                                                    #this is used for advanced table design
from reportlab.graphics.shapes import Drawing                                       #this is used for drawing, along with Pie make Pie graphs
from reportlab.graphics.charts.piecharts import Pie                                 #this is used for Pie, along with drawing make Pie graphs
from reportlab.lib.units import inch, cm                                            #this is used for assigning the converted values for inch and cm


#below will be variables needed for later

table_data = []

#this is what creates the blank pdf to build on, you can even give it an abs path + name to be more specific
report = SimpleDocTemplate("C:\\Users\\ADP55\\Desktop\\Master Scripts\\testfolder\\Testreport.pdf")
styles = getSampleStyleSheet()

fruit = {
"elder" : 1,
"apples" : 2,
"strawb" : 4,
"pineap" : 4,
"durian" : 5,
"bluebur": 3
}

#Creating flowables/chunks:

#Text
report_title = Paragraph("This is an Inventory of Available Fruit", styles["h1"])

#Table conversion from dictionary, tables want a list of lists aka 2d array
for k,v in fruit.items():
    table_data.append([k,v])

#Basic Table
report_table = Table(data=table_data)

#Adv Table
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

report_table2 = Table(data=table_data, style=table_style, hAlign="LEFT")

#Pie Graph
#creates a blank pie graph, needs data and labels
report_pie = Pie(width=3*inch, height=3*inch)

report_pie.data = []
report_pie.labels = []

#sorts data from dictionary fruit into separate lists for data and labels
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

#we need to first add a blank drawing (might be considered a flowable) then add our pie graph to it    
report_chart = Drawing()
report_chart.add(report_pie)

#Below here will be the build function that requires all flowables  passed to it in a list

report.build([report_title, report_table2, report_chart])


#%% Block 3 - Simple bring it all together Example



#%% Block 4 - Final Code Customized for Problem



















