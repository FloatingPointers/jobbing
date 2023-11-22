import base64
import token
from flask import Flask, make_response, redirect, request, jsonify, abort
from jobbing import app, db
from jobbing.models.user import User
import flask

from google.oauth2 import id_token
from google.auth.transport import requests
import jwt
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

@app.route('/login', methods=['POST'])
def google_auth():
    data = request.get_data().decode('utf-8')
    data = data.split("&")
    enc_creds = data[0].split("=")[1]
    g_csrf_token = data[1].split("=")[1]
    creds = jwt.decode(enc_creds, options={"verify_signature": False}, algorithms=["RS256"])
    
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
                    

    
    
    return flask.redirect("http://localhost:3000/login")


