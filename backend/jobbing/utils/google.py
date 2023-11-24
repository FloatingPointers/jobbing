import os

from dotenv import load_dotenv
import jwt

from jobbing.models.user import User
from jobbing.utils.constants import API_OAUTH, API_OAUTH_VERSION, SCOPES, TOKEN_URI
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
    with build(API_OAUTH, API_OAUTH_VERSION, credentials=credentials) as service:
        info = service.userinfo().get().execute()
    
    return info

def get_id(jwt_token: str):
    return jwt.decode(jwt_token, os.getenv("SECRET_KEY").encode('utf-8'), algorithms=["HS256"]).get('id')
