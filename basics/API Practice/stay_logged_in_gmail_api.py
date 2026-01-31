# stay_logged_in_gmail_api

# https://github.com/googleapis/google-api-python-client/blob/main/docs/oauth-installed.md
# https://github.com/googleapis/google-api-python-client/blob/main/docs/client-secrets.md

import google.auth
import google_auth_oauthlib.flow as Flow
import google.oauth2.credentials
from googleapiclient.discovery import build

# keep script running
leave = False 

# keep track of login status
logged_in = False

# initialize session, creds, and token
session = None
creds = None
token = 0

while leave != True:

    get_input = int(input('Option (0 leave, 1 choices): '))
    
    # exit
    if get_input == 0:

        if logged_in == True:
            session.close() 
        
        leave = True

    # show options
    if get_input == 1:

        print('0 exit')
        print('1 show options')
        print('2 Google login')
        print('3 token login')
        print('4 show user')
        print('5 logout')
        print('6 get creds')
        print('7 print labels')
        print('8 print messages')
    
    # Google login
    if get_input == 2:

        if logged_in == True:
            print('You are already logged in.')
        
        else:   
            SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.profile', 
                'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/gmail.readonly']
            
            flow = ggl_flow.InstalledAppFlow.from_client_secrets_file(
                    "login\\credentials.json", SCOPES
                )
            
            # opens browser for the user to sign in
            creds = flow.run_local_server(
                host='localhost',
                port=8080, 
                authorization_prompt_message='Please visit this URL: {url}', 
                success_message='The auth flow is complete; you may close this window.',
                open_browser=True
                )

            # set the token for no manuel login later
            token = creds.token

            session = flow.authorized_session()

            logged_in = True

            print('Google login successful!')

    # token login (doesn't require the user to sign in through google again)
    if get_input == 3:

        if token != 0:
            # get required credentials through token (expires, but can be refreshed)
            # client_id and client_secret need to be protected!!!!!!!
            creds = google.oauth2.credentials.Credentials(token)
            logged_in = True
            print('Token login successful!')

        else:
            print('You need to login through Google first to get token.')

    # show user
    if get_input == 4:

        if logged_in:

            # gets user info by making HTTP GET request
            user_info = session.get('https://www.googleapis.com/oauth2/v2/userinfo').json()

            for key, value in user_info.items():
                print(f'{key}: {value}')

        else:

            print('You are not logged in.')
    
    # logout
    if get_input == 5:

        if logged_in == False:
            print('You are already logged out.')

        else:
            # always close the session to prevent unnecessary data usage
            session.close()
            creds = None
            logged_in = False
            print('You are logged out, thanks for coming!')

    # get creds
    if get_input == 6:

        if logged_in == False or not creds:
            print('You are not logged in.')

        else:
            # show the current credentials being used
            print(creds.to_json())

    # print labels
    if get_input == 7:

        if logged_in == False or not creds:
            print('You are not logged in.')

        else:
            # create a connection to a specific API using it's name and verions
            # the token from the credentials is required
            service = build("gmail", "v1", credentials=creds)

            # this uses Python specific syntax rather than HTTP GET
            # this lists all labes used by a specific user (execute is necessary to run the command)
            results = service.users().labels().list(userId="me").execute()

            # retrieve the labes in a list
            labels = results.get("labels", [])

            for label in labels[0:3]:
                print(label)

    # print messages
    if get_input == 8:

        if logged_in == False or not creds:
            print('You are not logged in.')

        else:
            
            service = build("gmail", "v1", credentials=creds)
            
            print('Python-like')
            results_msg = service.users().messages().list(userId = 'me').execute()

            msg = results_msg.get("messages", [])

            for m in msg[0:3]:
                print(m['id'])

            print('Web-like')
            messages = session.get('https://gmail.googleapis.com/gmail/v1/users/me/messages').json()

            print(type(messages))
            # messages was a dictionary and the messages key is a list of dictionaries!!!
            for email in messages['messages'][0:3]:
                print(email['id'])


# https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html
# another example
# from google_auth_oauthlib.flow import Flow

# # Create the flow using the client secrets file from the Google API
# # Console.
# flow = Flow.from_client_secrets_file(
#     'path/to/client_secrets.json',
#     scopes=['profile', 'email'],
#     redirect_uri='urn:ietf:wg:oauth:2.0:oob')

# # Tell the user to go to the authorization URL.
# auth_url, _ = flow.authorization_url(prompt='consent')

# print('Please go to this URL: {}'.format(auth_url))

# # The user will get an authorization code. This code is used to get the
# # access token.
# code = input('Enter the authorization code: ')
# flow.fetch_token(code=code)

# # You can use flow.credentials, or you can just get a requests session
# # using flow.authorized_session.
# session = flow.authorized_session()
# print(session.get('https://www.googleapis.com/userinfo/v2/me').json())