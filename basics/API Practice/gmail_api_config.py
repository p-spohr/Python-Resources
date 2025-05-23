# %%

import os.path

import json

import google as ggl
import googleapiclient as ggl_client
import google_auth_oauthlib.flow as ggl_flow
from googleapiclient.discovery import build

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.errors import HttpError

# %%

GGL_REQUEST = ggl.auth.transport.requests.Request()

# %%

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
  
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  
  creds = None

  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("login\\token.json"):
    creds = ggl.oauth2.credentials.Credentials.from_authorized_user_file("login\\token.json", SCOPES)
    # creds = Credentials.from_authorized_user_file("login\\token.json", SCOPES)

  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(GGL_REQUEST)
    
    else:
      flow = ggl_flow.InstalledAppFlow.from_client_secrets_file(
          "login\\credentials.json", SCOPES
      )
      
      creds = flow.run_local_server(port=0)
    
    # Save the credentials for the next run
    with open("login\\token.json", "w") as token:
      token.write(creds.to_json())

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    for label in labels[0:2]:
      print(label)

    results_msg = service.users().messages().list(userId = 'me').execute()

    msg = results_msg.get("messages", [])

    for m in msg[0:2]:
      print(m['id'])

    print(service)
    print(service.users())
    print(service.users().messages())
    # print(service.users().messages().get(userId = 'me', id = '1924e102b2174058').execute()) # returns massive json
    # print(service.users().messages().get(userId = 'me', id = '1924e102b2174058')) # without execute() it is just a HttpRequest object

    print(service.users().messages().get(userId = 'me', id = '1924e102b2174058').execute()['snippet'])
    print(service.users().messages().get(userId = 'me', id = '1924e102b2174058').execute()['internalDate'])
    print(service.users().messages().get(userId = 'me', id = '1924e102b2174058').execute()['sizeEstimate'])

    with open('my_gmail_message.json', 'w') as mgm:
        json.dump(service.users().messages().get(userId = 'me', id = msg[0]['id'], format = 'raw').execute(), mgm)
    

    # I DID IT!!!!!
    print(service.users().messages().get(userId = 'me', id = msg[0]['id']).execute()['snippet'])
    
    # print(json.dump(service.users().messages().get(userId = 'me', id = '1924e102b2174058').execute()))

  except ggl_client.errors.HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()

# %%
