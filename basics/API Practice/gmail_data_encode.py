# encode file json
# %%

import email.iterators
import json
import base64
import email

# %%

with open('my_gmail_message.json', 'r') as gmail_msg:
    gmail_json = json.load(gmail_msg)

# %%

gmail_json

# %%

gmail_json.keys()

# %%

gmail_json['raw']

# %%
my_email = email.message_from_bytes(base64.urlsafe_b64decode(gmail_json['raw']))

# %%

my_email.keys()

# %%

my_email.values()

# %%

my_email.is_multipart()

# %%

email.iterators._structure(my_email)

# %%

my_email.get_content_maintype()

# %%

type(my_email.get_content_maintype())

# %%

print(my_email.get_payload()[1])

# %%

print("----------------------------------------------------")

# Find full message body

message_main_type = my_email.get_content_maintype()

if message_main_type == 'multipart':
    for part in my_email.get_payload():
        if part.get_content_maintype() == 'text':
            print(part.get_payload())
elif message_main_type == 'text':
    print(my_email.get_payload())

print("----------------------------------------------------")