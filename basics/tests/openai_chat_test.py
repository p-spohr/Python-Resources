# openai_chat_test

# %%

import openai
import base64
import requests
import json
from login import openai_login

# %%

client = openai.OpenAI(
    api_key= openai_login.API_KEY
    # organization= openai_login.ORG_ID,
    # project= openai_login.PROJECT_ID,
)

# %%

client.models.list().to_dict().values()

# %%

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "I'm going to say three numbers."
                    },
               
            ],
        },

        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "1"
                    },
               
            ],
        },

        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "2"
                    },
               
            ],
        },

        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "10"
                    },
               
            ],
        },

        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "What is the sum of the three numbers?"
                    },
               
            ],
        }

    ],
    max_tokens=300,
)


# %%

print(response.to_dict()['choices'][0]['message']['content'])

# %%
my_image = 'C:\\Users\\pat_h\\skyline.jpg'

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

prepared_image = encode_image(my_image)

# %%

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
my_image_path = "C:\\Users\\pat_h\\skyline.jpg"

# Getting the base64 string
base64_image = encode_image(my_image_path)

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
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

# %%

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
          "text": "What is a rainbow?"
        }
      ]
    }
  ],
  "max_tokens": 300
}

# %%

payload_json = json.dumps(payload)

# %%

response = requests.post(
  "https://api.openai.com/v1/chat/completions", 
  headers=headers, 
  data=payload_json)

# %%

type(response)

# %%

json.loads(response.text)

# %%
response.request.body

# %%
response.json()['choices'][0]['message']['content']


# %%
print(response.json())


# %%

print(response.json().keys())

# %%

print(response.json()['choices'][0]['message']['content'])



# %%
