from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from smtplib import SMTP
from flask_bcrypt import Bcrypt
from model import connect_to_db,User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app=Flask(__name__)

#app.config['SECRET_KEY']='this is techno db'
app.secret_key="this is techno db"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/user.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://techno:123456@localhost:5433/technoapp'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'tno635788@gmail.com'
# app.config['MAIL_PASSWORD'] = 'qgujfqjxyswrfzce'

print("1------------------------")

#db= SQLAlchemy(app)
print("2------------------------")

login_manager = LoginManager(app)
mail = Mail(app)
bcrypt=Bcrypt(app)
print("3------------------------")



@login_manager.unauthorized_handler
def unauthorized():
   
    return redirect(url_for('Loginpage'))

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


if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True)
    import route   
    connect_to_db(app)
    app.run(host="127.0.0.1", port=5001, debug=True)
