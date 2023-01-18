from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin



db = SQLAlchemy()
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False) 
    image_file = db.Column(db.String(20), nullable= False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

     

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

def connect_to_db(flask_app, db_name= "technoapp", echo=True):
    db_uri = f'postgresql:///{db_name}'

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

