from flask_sqlalchemy import SQLAlchemy
from test3 import db, app
from test3 import login_manager
from flask import Flask, redirect, url_for
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer



db = SQLAlchemy(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
   
    return redirect(url_for('Loginpage'))

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False) 
    image_file = db.Column(db.String(20), nullable= False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
  
    def get_token(self, expires_sec=300):
        serial = Serializer(app.config['SECRET_KEY'], expires_in = expires_sec)
        return serial.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        serial = Serializer(app.config['SECRET_KEY'])
        try:
            user_id=serial.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

     

    def __repr__(self):
        return f'{self.username}:{self.email}:{self.date_created}'

class Ios(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    prosubios = db.Column(db.String(100), nullable=False) 
    proios = db.Column(db.String(500), nullable=False)  

    def __repr__(self):
        return f'{self.prosubios}:{self.proios}'

class Android(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    prosubandroid = db.Column(db.String(100), nullable=False) 
    proandroid = db.Column(db.String(500), nullable=False)  

    def __repr__(self):
        return f'{self.prosubandroid}:{self.proandroid}'

class ContactUs(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False) 
    email = db.Column(db.String(500), nullable=False)  
    msg = db.Column(db.String(500), nullable=False)  

    def __repr__(self):
        return f'{self.username}:{self.email}:{self.msg}'

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)