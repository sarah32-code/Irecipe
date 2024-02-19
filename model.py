from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from secret_key import secret_key
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer



db = SQLAlchemy()

def get_serializer(expires_sec=300):
    return Serializer(secret_key, expires_in = expires_sec)


class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False) 
    image_file = db.Column(db.String(20), nullable= False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    graphical_password = db.Column(db.String(128), nullable=True)  # Store image choices as string
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    
    def set_graphical_password(self, image_choices):
        """Set the graphical password."""
        self.graphical_password = ','.join(image_choices)

    def check_graphical_password(self, image_choices):
        """Check if the given image choices match the stored graphical password."""
        if self.graphical_password:
            stored_choices = self.graphical_password.split(',')
            return stored_choices == image_choices
        return False  # Return False if graphical password is not set

    def get_token(self, expires_sec=300):
        serial = get_serializer(expires_sec)
        return serial.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        serial = get_serializer()
        try:
            user_id=serial.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)    

    def __repr__(self):
        return f'{self.username}:{self.email}:{self.date_created}'

class Fish(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    prosubfish = db.Column(db.String(100), nullable=False) 
    profish = db.Column(db.String(500), nullable=False)  

    def __repr__(self):
        return f'{self.prosubfish}:{self.profish}'

class Chicken(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    prosubchicken = db.Column(db.String(100), nullable=False) 
    prohicken = db.Column(db.String(500), nullable=False)  

    def __repr__(self):
        return f'{self.prosubchicken}:{self.prochicken}'

class Meat(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    prosubmeat = db.Column(db.String(100), nullable=False) 
    promeat = db.Column(db.String(500), nullable=False)  

    def __repr__(self):
        return f'{self.prosubmeat}:{self.promeat}'  

class ContactUs(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False) 
    email = db.Column(db.String(500), nullable=False)  
    msg = db.Column(db.String(500), nullable=False)  

    def __repr__(self):
        return f'{self.username}:{self.email}:{self.msg}'

def connect_to_db(flask_app, db_name="SM", echo=True):
    db_uri = f"mysql://root:12345678@localhost/{db_name}"

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")