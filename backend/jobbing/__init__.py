"""Initialize Flask app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY").encode('utf-8')
app.config.from_object('jobbing.config')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:admin@127.0.0.1:3306/jobbing"

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

from jobbing.models.user import User
with app.app_context():
    db.create_all()

import jobbing.routes


