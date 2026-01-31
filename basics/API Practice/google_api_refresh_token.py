
# %%

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

# %%

creds = Credentials.from_authorized_user_file(
    "login\\token.json", 
    ["https://www.googleapis.com/auth/gmail.readonly"]
)

# %%

creds.valid

# %%

creds.expired

# %%

creds.refresh(Request())

# %%

creds.valid

# %%

creds.expired

# %%

creds.to_json()