# gmail_api_testing

# %%

import google_auth_oauthlib.flow as ggl_flow

# %%

SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.profile', 
          'https://www.googleapis.com/auth/userinfo.email']

flow = ggl_flow.InstalledAppFlow.from_client_secrets_file(
          "login\\credentials.json", SCOPES
      )
      
creds = flow.run_local_server(port=0)

session = flow.authorized_session()

print(session.get('https://www.googleapis.com/oauth2/v2/userinfo').json())

session.close()

# %%

SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.profile', 
          'https://www.googleapis.com/auth/userinfo.email']

flow = ggl_flow.InstalledAppFlow.from_client_secrets_file(
          "login\\credentials.json", SCOPES
      )
      
creds = flow.run_local_server(host='localhost',
    port=8080, 
    authorization_prompt_message='Please visit this URL: {url}', 
    success_message='The auth flow is complete; you may close this window.',
    open_browser=True)

session = flow.authorized_session()

print(session.get('https://www.googleapis.com/oauth2/v2/userinfo').json())

session.close()

# %%

