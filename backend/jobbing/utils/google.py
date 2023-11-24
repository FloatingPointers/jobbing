import os

from dotenv import load_dotenv

from backend.jobbing.models.user import User
from backend.jobbing.utils.constants import SCOPES, TOKEN_URI
load_dotenv()

def get_credentials(id: str):
    """Create a credentials json for a user for api requests."""
    user = User.query.filter_by(id=id).first()
    if not user:
        raise ValueError("User does not exist.")
    credentials = {
        "token": user.token,
        "refresh_token": user.refresh_token,
        "token_uri": TOKEN_URI,
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
        "scopes": SCOPES,
    }
    
    return credentials

def get_user_info(id: str):
    """Get user info from Google API."""
    credentials = get_credentials(id)
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    credentials = Credentials(**credentials)
    with build('oauth2', 'v2', credentials=credentials) as service:
        info = service.userinfo().get().execute()
    
    return info
