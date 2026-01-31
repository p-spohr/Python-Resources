# gmail_api_testing

# %%

import google as ggl
import inspect
import json

# %%

false_creds = ggl.oauth2.credentials.Credentials.from_authorized_user_file("login\\token_false.json")


# %%

type(false_creds)

# %%

dir(false_creds)

# %%

inspect.ismodule(false_creds)

# %%

inspect.isclass(false_creds)

# %%

inspect.ismethod(false_creds)

# %%
 
inspect.isfunction(false_creds)

# %%

false_creds_dict = dict(inspect.getmembers(false_creds))

# %%

for key, value in false_creds_dict.items():
    if key[0] != '_':
        print(f'{key} : {value}')

# %%
with open('login\\token_false.json') as tk_fl:
    for key, value in json.load(tk_fl).items():
        print(f'{key} : {value}')


# %%

false_creds.valid

# %%

false_creds.expired

# %%

import google_auth_oauthlib.flow as ggl_flow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

flow = ggl_flow.InstalledAppFlow.from_client_secrets_file(
          "login\\credentials.json", SCOPES
      )
      
true_creds = flow.run_local_server(port=0)

service = build("gmail", "v1", credentials= true_creds)
results = service.users().labels().list(userId="me").execute()
labels = results.get("labels", [])

for label in labels:
    print(label)

service.close()

# %%

print(service)

# %%

# %%
