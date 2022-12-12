from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from test3.forms import RegistrationForm, LoginForm
app=Flask(__name__)

app.config['SECRET_KEY']='this is techno db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)

from test3 import route