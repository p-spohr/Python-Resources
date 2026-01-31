#### Describes Images Sent to Gmail Using AI and Sends the Sender a Description
# requires the email subjects to have the required code
# works for jpeg and png image formats
# %%

# login to the app through the browser and Google
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# class for constructing email messages
from email.message import EmailMessage

# encode and decode data from Gmail and OpenAI API
import base64

# needed for passing argument into python script
import sys

# openai API access and login info
import openai
from login import openai_login

# get credentials and refresh tokens if expired
import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

import google_auth_oauthlib.flow as Flow


# keep track of OpenAI request time
import time

#### Autheticate Gmail API credentials
# %%

# argument passed into py script (CODE_REQUEST)
# only emails with the required code_request will get analyzed
try:
    CODE_REQUEST = sys.argv[1]

    if len(CODE_REQUEST) != 6:
        exit()

except:

    print('Please provide necessary 6 character code.')
    exit()

# complete scope for gmail
SCOPES = ['https://mail.google.com/']

# %%

# prepare to check credentials
creds = None

# get token to access Gmail API or ask the user to sign in using Google if not available
if os.path.exists("login\\gmail_token.json"):

    try:

        creds = Credentials.from_authorized_user_file("login\\gmail_token.json", SCOPES)
        print('Credentials successfully retrieved!')
        
        if creds.expired == False:
            print('Token is current and does not need to be refreshed.')

    except:

        print('Credentials could not be retrieved from file. Try again.')
        exit()

    if creds.expired == True or creds.valid == False or creds == None:
        
        try:

            creds.refresh(Request())
            print('Expired token successfuly refreshed!')

        except:

            print('Credentials could not be refreshed. Please log in to Google Account.')
            
            flow = Flow.InstalledAppFlow.from_client_secrets_file(
            "login\\credentials.json", SCOPES
            )
            
            try:

                creds = flow.run_local_server(
                    host='localhost',
                    port=8080, 
                    authorization_prompt_message='Please visit this URL: {url}', 
                    success_message='The auth flow is complete; you may close this window.',
                    open_browser=True
                    )

                with open('login\\gmail_token.json', 'w') as token:

                    token.write(creds.to_json())

            except:

                print('Could not log into Google Account. Please Try again.')

else:

    flow = InstalledAppFlow.from_client_secrets_file('login\\credentials.json', SCOPES)

    creds = flow.run_local_server(
                    host='localhost',
                    port=8080, 
                    authorization_prompt_message='Please visit this URL: {url}', 
                    success_message='The auth flow is complete; you may close this window.',
                    open_browser=True
                    )
    with open('login\\gmail_token.json', 'w') as gmail_token:

        gmail_token.write(creds.to_json())

#### Get all message ids with the correct code
# %%

try:

    service = build('gmail', 'v1', credentials= creds)
    print('Connection to Gmail successful!')

except:

    print('Connection to Gmail API failed. Try again.')
    exit()

# %%

# service.users().labels().list(userId = 'me').execute()


# %%

try:
    # List of messages. Note that each message resource contains only an id and a threadId.
    messages = service.users().messages().list(userId= 'me', maxResults = 30, labelIds = ['INBOX']).execute()
    
    print(f'{len(messages['messages'])} Gmail messages retrieved successfully.')


except:
    print('Gmail API could not retrieve messages. Try again.')
    exit()


# %%
messages_list = messages['messages']
newest_messages = []

for msg in messages_list:
    newest_messages.append(msg['id'])


# %%

mime_email = []

# list() only gets id info, so the IDs need to be passed into get() to get full message
try:

    for msg_id in newest_messages:
        mime_email.append(service.users().messages().get(userId = 'me', id = msg_id).execute())

    print('Message packages have been retrieved successfully by ID.')

except:

    print('Message packages could not be retrieved. Try again.')


# %%

target_emails = []

for msg in mime_email:

    for header in msg['payload']['headers']:

        if header['name'].lower() == 'subject' and header['value'] == CODE_REQUEST:

            target_emails.append(msg)


# %%

msg_ids = []
msg_sender_emails = []

for msg in target_emails:

   msg_ids.append(msg['id'])
   
   for header in msg['payload']['headers']:
    
        if header['name'].lower() == 'from':
            msg_sender_emails.append(header['value'])

if len(msg_ids) < 1:
    print('No emails identified with correct code.')
    exit()
else:
    print(f'{len(msg_ids)} emails identified with the request code {CODE_REQUEST}.')


# %%

# the attatchment IDs are appended if the message IDs have the correct code as subject
msg_attachment_ids = []
msg_attachment_names = []

for msg in target_emails:
    
    has_attachment = False

    for part in msg['payload']['parts']:

        if part['mimeType'].split('/')[0] == 'image':

            has_attachment = True
            
    if has_attachment:     
        
        msg_attachment_ids.append(msg['payload']['parts'][1]['body']['attachmentId'])
        msg_attachment_names.append(msg['payload']['parts'][1]['filename'])

    else:
        msg_attachment_ids.append('EMPTY')
        msg_attachment_names.append('EMPTY')
 

id_package = zip(msg_ids, msg_sender_emails, msg_attachment_ids)


# %%

#### Use ids to get sender email and picture data
image_data = []
for m_id, s_email, a_id in id_package:
    
    if a_id != 'EMPTY':
        
        data = service.users().messages().attachments().get(userId= 'me', messageId = m_id, id= a_id).execute()
        image_data.append(data)
    
    else:
        image_data.append('EMPTY')

# Prepare images for OpenAI API and send for completion
# %%

openai_prepared_images = []
email_ready_images = []

for i_data in image_data:

    if i_data != 'EMPTY':
        
        # urlsafe b64decode is different from standard b64decode
        pic_decoded = base64.urlsafe_b64decode(i_data['data']) 
        pic_encoded = base64.b64encode(pic_decoded)

        # these image as bytes will be used later to attach the picture to the return email
        email_ready_images.append(pic_decoded)

        # these str of base64 images are sent to the OpenAI API to be analyzed
        prepared_pic = pic_encoded.decode('utf-8')
        openai_prepared_images.append(prepared_pic)

    else:

        # ignore emails that have code but no attachment
        openai_prepared_images.append('EMPTY')
        email_ready_images.append('EMPTY')


# %%

try:

    client = openai.OpenAI(
        api_key= openai_login.API_KEY
    )

except:

    print('Cannot connect to OpenAI client')

# %%

# count how many emails have no attachment
empty_count = 0
for prepared_image in openai_prepared_images:
    if prepared_image == 'EMPTY':
        empty_count += 1


# %%

# prepare to send image data to OpenAI API
openai_request_images = zip(openai_prepared_images, msg_attachment_names)

start_time = time.time()
print('Sending request to OpenAI API...')

try:
    
    openai_responses = []
    i = 0
        
    for prepared_image, image_name in openai_request_images:
        
        
        # ignore emails without attachement
        if prepared_image != 'EMPTY':

            img_extension = image_name.split('.')[1]

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
                                "text": "Use the following format example: A Big Dog on a Bench;This is an image of a large brown dog sitting on a dark brown bench and it appears to be in a park or somewhere where there is a lot of pleasant greenery."
                            },
                            {
                                "type": "text", 
                                "text": "This is another example: Colorful Hot Air Balloon in the Sky;One can see a colorful hot air balloon with a colorful mosaic pattern flying in a clear blue sky above a mountainous landscape."
                            },
                            {
                                "type": "text", 
                                "text": "Describe the image with the following format, no additional symbols, quotes, or new lines: title of image;description of image"
                            },
                            {
                                "type": "image_url",
                                "image_url": 
                                {
                                    "url": f"data:image/{img_extension};base64,{prepared_image}"
                                }
                            },
                        ],
                    }
                ],
                max_tokens=300,
            )

            openai_responses.append(response.choices[0].message.content)

            # keep track of processed images
            i += 1
            print(f'Progress: {i}/{len(openai_prepared_images) - empty_count} images analyzed.')
        
        else:

            openai_responses.append('EMPTY')
            
except:
    
    print('OpenAI connection failed. Try again')
    print('Exiting...')
    exit()

end_time = time.time()

print(f'OpenAI request took {round(end_time - start_time, 2)} seconds.')

#### Organize responses with sender email
# %%

print('Preparing emails...')

cleaned_emails = []

for email in msg_sender_emails:
    
    if '<' in email:
        cleaned_emails.append(email.split('<')[1][0:-1])
    
    else:
        cleaned_emails.append(email)


# %%

send_email_package = zip(cleaned_emails, openai_responses, email_ready_images, msg_attachment_names)

#### Send email with response
# %%

email_from = 'Image Describer 2024 <spohrpatrick@gmail.com>'

for sender_email, openai_response, email_image, attachment_name in send_email_package:

    # https://docs.python.org/3/library/email.message.html
    # prepare email content manager
    message = EmailMessage()
    
    user_name = sender_email.split('@')[0]

    if openai_response != 'EMPTY':

        response_title, response_body = openai_response.split(';')

        message.add_header('To', sender_email)
        message.add_header('From', email_from)
        message.add_header('Subject', f'{response_title}')

        smile_emoji = '&#128512;'
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Responsive Email Template</title>
        </head>
        <body>
            <h1>{response_title}</h1>
            <h2>Dear {user_name},</h2>
            <p style = "font-weight:bold;">Here is the description of your image:</p>
            <p>{response_body}</p>
            <h2>{smile_emoji}  {smile_emoji}  {smile_emoji}</h2>
            <h4>Thank you for using Image Describer!</h4>
        </body>
        </html>
        """

        file_extension = attachment_name.split('.')[1]
        file_name = f'{response_title}.{file_extension}'

        message.add_header('Content-Disposition', f'attachment;filename={file_name}')

        # set plain/text content for if HTML doesn't load
        message.set_content(f'Dear {user_name}, here is the description of your image: {response_body} --- Thank you! Have a nice day!')
        
        # use HTML content instead of plain/text
        message.add_alternative(html_content, subtype = 'html') 
        
        # email_image is of type bytes and that means maintype and subtype are required
        message.add_attachment(email_image, maintype = 'image', subtype = file_extension, filename = file_name)


    else:

        message.add_header('To', sender_email)
        message.add_header('From', email_from)
        message.add_header('Subject', 'Please attach image')
        
        message.set_content(f'Dear {user_name}, please resend email with attached image to be analyzed --- Thank you! Have a nice day!')

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    raw_message = {'raw': encoded_message}

    # pylint: disable=E1101
    try:
        send_message = service.users().messages().send(userId = 'me', body = raw_message).execute()
    except:
        print(f'Could not send {sender_email} an email.')
        
    if 'SENT' in send_message['labelIds']:
        if attachment_name != 'EMPTY':
            print(f'"{response_title}" sent successfully to {sender_email}!')
        else:
            print(f'Reminder to add attachment sent to {sender_email}.')
    else:
        print(f'{sender_email} did not recieve email.')
    

# close the API connection
service.close()

# %%
