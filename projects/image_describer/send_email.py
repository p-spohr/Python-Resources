# send_email

# %%

import smtplib
import ssl
from login import gmail_login

from email.message import EmailMessage

import base64
from email.mime.image import MIMEImage

import inspect
import mimetypes

# %%

HOST = 'smtp.gmail.com'
PORT = 465  # For SSL
PASSWORD = gmail_login.APP_PASSWORD
MY_EMAIL = gmail_login.GMAIL

# Create a secure SSL context
CONTEXT = ssl.create_default_context()

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Email Template</title>
</head>
<body>
    <h1 style = "text-align:center;">Center Header</h1>
    <p style = "color:blue;text-decoration:underline;">This should be blue.</p>
    <p style = "font-weight:bold;">IS IT WORKING?!</p>
    <img src="https://picsum.photos/536/354" title="Test Image"></img>
    <h3>Thank you!</h3>
</body>
</html>
"""

# %%

mtype, stype = mimetypes.guess_type('cheez.jpg')

extension = mimetypes.guess_extension(mtype)


#%%


with open('cheez.jpg', 'rb') as pic:
    mime_image = MIMEImage(pic.read())

# %%

with open('cheez.jpg', 'rb') as pic:
    b_image = pic.read()

# %%

my_message = EmailMessage()

my_message.add_header('From', MY_EMAIL)
my_message.add_header('To', MY_EMAIL)
my_message.add_header('Subject', 'HTML Content Test')
my_message.add_header('Content-Disposition', 'attachment; filename="cheez.jpg')

my_message.set_content('This is just text.')
# my_message.add_alternative(html_content, subtype= 'html')

my_message.add_attachment(b_image, maintype = 'image', subtype = 'jpeg', filename = 'cheez.jpg')


# %%


with smtplib.SMTP_SSL(HOST, PORT, context=CONTEXT) as server:
    server.login(MY_EMAIL, PASSWORD)
    server.send_message(msg= my_message)
    # server.sendmail(my_email, gmail_login.HOTMAIL, msg= 'SECOND TEST!')
    print('Email sent!')
    

# %%

# https://www.geeksforgeeks.org/how-to-display-base64-images-in-html/
# <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA..."/>
# example for using base64 images
# %%
