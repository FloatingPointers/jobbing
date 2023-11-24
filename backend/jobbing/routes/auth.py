import base64
import token
from flask import Flask, make_response, redirect, request, jsonify, abort, session
import google_auth_oauthlib
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
    flow.redirect_uri = flask.url_for('login', _external=True)

    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in the session.
    # ACTION ITEM for developers:
    #     Store user's access and refresh tokens in your data store if
    #     incorporating this code into your real app.
    credentials = flow.credentials
    print(credentials)
    
    info = None
    with build('oauth2', 'v2', credentials=credentials) as service:
        info = service.userinfo().get().execute()
    
    # ID token is valid. Get the user's Google Account ID from the decoded token
    user_id = info.get('id')
    email = info.get('email')
    name = info.get('name')
        
    # Check if user exists in database
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(id=user_id, email=email, name=name)
        db.session.add(user)
        db.session.commit()
    
    # Create JWT token
    jwt_token = jwt.encode({"id": user.id}, os.getenv("SECRET_KEY").encode('utf-8'), algorithm="HS256")
    
    # Set JWT token in cookie
    resp = make_response(redirect('http://localhost:3000/'))
    resp.set_cookie('jwt_token', jwt_token, httponly=True, secure=True, samesite='None')
    
    return resp

@app.route('/login', methods=['POST'])
def login():
    data = request.get_data().decode('utf-8')
    print(data)
    scope = request.form["scope"]
    enc_creds = request.form["credential"]
    g_csrf_token = request.form["g_csrf_token"]
    # creds = jwt.decode(enc_creds, options={"verify_signature": False}, algorithms=["RS256"])
    
    csrf_token_cookie = request.cookies.get('g_csrf_token')
    if not csrf_token_cookie:
        flask.abort(400, 'No CSRF token in Cookie.')
    csrf_token_body = g_csrf_token
    if not csrf_token_body:
        flask.abort(400, 'No CSRF token in post body.')
    if csrf_token_cookie != csrf_token_body:
        flask.abort(400, 'Failed to verify double submit cookie.')
        
    idinfo = id_token.verify_oauth2_token(enc_creds, requests.Request(), os.getenv("CLIENT_ID"))
    
    # ID token is valid. Get the user's Google Account ID from the decoded token
    print(idinfo)
    userid = idinfo['sub']
    email = idinfo.get('email')
    name = idinfo.get('name')
    
    app.logger.info(userid)
    app.logger.info(email)
    app.logger.info(name)
        
    # Check if user exists in database
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(id=userid, email=email, name=name)
        db.session.add(user)
        db.session.commit()
    
    # Create JWT token
    jwt_token = jwt.encode({"id": user.id}, os.getenv("SECRET_KEY").encode('utf-8'), algorithm="HS256")
    
    # Set JWT token in cookie
    resp = make_response(redirect('http://localhost:3000/'))
    resp.set_cookie('jwt_token', jwt_token, httponly=True, secure=True, samesite='None')
    resp.set_cookie('g_csrf_token', g_csrf_token, httponly=False, secure=True, samesite='None')
    
    return resp