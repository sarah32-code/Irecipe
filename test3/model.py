from flask_sqlalchemy import SQLAlchemy
from test3 import db
from flask import Flask
from test3 import app



db = SQLAlchemy(app)
class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False) 
    password = db.Column(db.String(20), nullable=False) 

    def __repr__(self):
        return f'{self.username}:{self.email}'

class Ios(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    prosubios = db.Column(db.String(100), nullable=False) 
    proios = db.Column(db.String(500), nullable=False)  

    def __repr__(self):
        return f'{self.prosubios}:{self.proios}'

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)