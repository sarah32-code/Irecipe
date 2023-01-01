from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from smtplib import SMTP
from flask_bcrypt import Bcrypt
app=Flask(__name__)

app.config['SECRET_KEY']='this is techno db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/user.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://techno:123456@localhost:5433/technoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tno635788@gmail.com'
app.config['MAIL_PASSWORD'] = 'qgujfqjxyswrfzce'


db= SQLAlchemy(app)
login_manager = LoginManager(app)
mail = Mail(app)
bcrypt=Bcrypt(app)
from test3 import route   