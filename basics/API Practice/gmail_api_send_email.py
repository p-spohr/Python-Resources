# %%
# gmail_api_send_email

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import json
import base64

# %%

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# %%

token = Credentials.from_authorized_user_file(
    "login\\token.json", 
    SCOPES
)

# %%

token.valid

# %%

token.expired

# %%

token.refresh(Request())

# %%

token.valid

# %%

token.to_json()

# %%

service = build("gmail", "v1", credentials=token)
results = service.users().labels().list(userId="me").execute()
labels = results.get("labels", [])

for label in labels[0:2]:
    print(label)

# %% 

messages = service.users().messages().list(userId= 'me').execute()


# %%

messages_list = messages['messages']
newest_messages = []

for msg in messages_list[0:15]:
    print(msg['id'])
    newest_messages.append(msg['id'])


# %%

newest_messages
email = []
for msg_id in newest_messages:
    email.append(service.users().messages().get(userId = 'me', id = msg_id).execute())


# %%

for em in email:
    print(em['snippet'])


# %%

print(email[0])

with open('email_example_with_attachment.json', 'w') as email_json:
    email_json.write(json.dumps(email[0]))


# %%

with open('email_body_decoded_example', 'w') as email_decoded:
    
    email_bytes = base64.urlsafe_b64decode(email[0]['payload']['parts'][1]['body']['data'])
    
    email_str = email_bytes.decode('utf-8')

    email_decoded.write(email_str)

# %%

for i in range(0, len(email)):
    
    headers = email[i]['payload']['headers']
    
    for header in headers:
        if header['name'].lower() == 'subject' and header['value'] == '555':
            print('Check this email.')


# %%

attachment_id = email[0]['payload']['parts'][1]['body']['attachmentId']
email_id = email[0]['id']

# %%

service.users().messages().get(userId= 'me', id= email_id).execute()


# %%

attachment_json = service.users().messages().attachments().get(userId= 'me', messageId = email_id, id= attachment_id).execute()

# %%

from PIL import Image
import io

# %%

with open('my_pic.jpg', 'wb') as pic:
    pic.write(base64.urlsafe_b64decode(attachment_json['data']))


# %%
import openai
import requests
from login import openai_login
# %%

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# %%

prepared_pic = encode_image('my_pic.jpg')

# %%

non_path_pic_decoded = base64.urlsafe_b64decode(attachment_json['data'])
non_path_pic_encoded = base64.b64encode(non_path_pic_decoded)
prepared_pic_2 = non_path_pic_encoded.decode('utf-8')

# %%
# OpenAI Vison
# https://platform.openai.com/docs/guides/vision

client = openai.OpenAI(
    api_key= openai_login.API_KEY
    # organization= openai_login.ORG_ID,
    # project= openai_login.PROJECT_ID,
)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {openai_login.API_KEY}"
}

payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image? Describe it in one sentence."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{prepared_pic_2}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)


# %%

response.json()['choices'][0]['message']['content']

# %%

# %%

url_image_path = 'https://developers.google.com/static/identity/protocols/oauth2/images/flows/implicit.png'

client = openai.OpenAI(
    api_key= openai_login.API_KEY
    # organization= openai_login.ORG_ID,
    # project= openai_login.PROJECT_ID,
)

response_2 = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url_image_path,
                    }
                },
            ],
        }
    ],
    max_tokens=300,
)

# %%

response_2.choices[0].message.content


# %%

import openai
from login import openai_login

image_url_ballon = 'https://cdn.prod.website-files.com/64c82edd724cd267a8038611/65cc1ea2fd2eec76f0211034_Untitled%20design.jpg'
image_url_steak = 'https://cdn.shopify.com/s/files/1/1433/0188/files/2017_03_13_ES_-_TXOGITXU_-_Roastbeef_Su_003_1024x1024.jpg?v=1511867277'
image_url_football = 'https://www.aljazeera.com/wp-content/uploads/2022/11/2022-04-20T202058Z_1188430601_UP1EI4K1KIWO1_RTRMADP_3_SOCCER-ENGLAND-CHE-ARS-REPORT.jpg?resize=1920%2C1440'

client = openai.OpenAI(
    api_key= openai_login.API_KEY
    # organization= openai_login.ORG_ID,
    # project= openai_login.PROJECT_ID,
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "I will give you an image and I want you to describe it."
                },
                {
                    "type": "text", 
                    "text": "Use the following format example: A Big Dog on a Bench;This is an image of a large brown dog sitting on a bench. It appears to be in a park or somewhere where there is a lot of greenery."
                },
                {
                    "type": "text", 
                    "text": "This is another example: Colorful Hot Air Balloon in the Sky;This is an image of a colorful hot air balloon with a mosaic pattern flying in a clear blue sky above a mountainous landscape."
                },
                {
                    "type": "text", 
                    "text": "Describe the image with the following format, no additional symbols, quotes, or new lines: title of image;description of image"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url_ballon
                    }
                },
            ],
        }
    ],
    max_tokens=300,
)

content = response.choices[0].message.content.split(';')



# %%

content[0]

# %%
content[1]