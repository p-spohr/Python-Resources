# send_email

# %%

import smtplib
import ssl
from login import gmail_login

# %%

HOST = 'smtp.gmail.com'
PORT = 465  # For SSL
PASSWORD = gmail_login.APP_PASSWORD

# Create a secure SSL context
CONTEXT = ssl.create_default_context()

# %%

my_email = gmail_login.GMAIL

with smtplib.SMTP_SSL(HOST, PORT, context=CONTEXT) as server:
    server.login(my_email, PASSWORD)
    server.sendmail(my_email, gmail_login.HOTMAIL, msg= 'SECOND TEST!')

