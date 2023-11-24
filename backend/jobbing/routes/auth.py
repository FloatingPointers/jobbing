import base64
import token
from flask import Flask, make_response, redirect, request, jsonify, abort, session
import google_auth_oauthlib
from jobbing.utils.constants import API_OAUTH, API_OAUTH_VERSION
from jobbing import app, db
from jobbing.models.user import User
import flask
from googleapiclient.discovery import build


from google.oauth2 import id_token
from google.auth.transport import requests
import jwt
from dotenv import load_dotenv
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
# Load environment variables from the .env file
load_dotenv()

@app.route('/login', methods=['GET', 'POST'])
def google_auth():
    data = None
    if request.method == 'GET':
        data = request.args
    elif request.method == 'POST':
        data = request.form
    # print(data)
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=data['scope'],
        state=data['state'],
        )
    flow.redirect_uri = flask.url_for('google_auth', _external=True)

    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in the session.
    # ACTION ITEM for developers:
    #     Store user's access and refresh tokens in your data store if
    #     incorporating this code into your real app.
    credentials = flow.credentials
    print(credentials)
    
    info = None
    with build(API_OAUTH, API_OAUTH_VERSION, credentials=credentials) as service:
        info = service.userinfo().get().execute()
    
    # ID token is valid. Get the user's Google Account ID from the decoded token
    user_id = info.get('id')
    email = info.get('email')
    name = info.get('name')
    
    # Check if user exists in database
    user = User.query.filter_by(id=user_id).first()
    if not user:
        user = User(id=user_id,
                    email=email,
                    name=name,
                    given_name=info.get('given_name'),
                    token=credentials.token,
                    refresh_token=credentials.refresh_token,
                    picture=info.get('picture'),
                    )
        db.session.add(user)
        db.session.commit()
    
    # Create JWT token
    jwt_token = jwt.encode({"id": user.id}, os.getenv("SECRET_KEY").encode('utf-8'), algorithm="HS256")
    
    # Set JWT token in cookie
    resp = make_response(redirect('http://localhost:3000/jobbing'))
    resp.set_cookie('jwt_token', jwt_token, httponly=True, secure=True, samesite='None')
    return resp

