from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email,ValidationError
from model import User
from flask_login import login_user, logout_user, current_user, login_required
 
class RegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField(label= 'Email',validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',validators=[DataRequired(), Length(min=3, max=20)])
    confirm_password = PasswordField(label= 'confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label= 'Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError ('This user is taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError ('This email is taken')

class LoginForm(FlaskForm):
    email = StringField(label= 'Email',validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField(label= 'Login')  

class IosForm(FlaskForm):
    prosubios = StringField(label= 'Subject',validators=[DataRequired(), Length(min=3, max=50)])
    proios = StringField(label='Your solution',validators=[DataRequired(), Length(min=10, max=300)])
    submit = SubmitField(label= 'Add solution')
      

class AndroidForm(FlaskForm):
    prosubandroid = StringField(label= 'Subject',validators=[DataRequired(), Length(min=3, max=50)])
    proandroid = StringField(label='Your solution',validators=[DataRequired(), Length(min=3, max=300)])
    submit = SubmitField(label= 'Add solution')   

class ContactUsForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField(label= 'Email',validators=[DataRequired(), Email()])
    msg = StringField(label='Write your Message',validators=[DataRequired(), Length(min=3, max=100)])
    submit = SubmitField(label= 'Send')

class SearchForm(FlaskForm):
    searched = StringField(label= 'Searched',validators=[DataRequired()])
    submit = SubmitField(label= 'Add solution') 

class ResetRequestForm(FlaskForm):
    email = StringField(label= 'Email',validators=[DataRequired()])
    submit = SubmitField(label= 'Reset Password',validators=[DataRequired()]) 
    
class ResetPasswordForm(FlaskForm):
    password = PasswordField(label='Password',validators=[DataRequired(), Length(min=3, max=20)])
    confirm_password = PasswordField(label= 'Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label= 'Reset password')  

class AccountForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField(label= 'Email',validators=[DataRequired(), Email()])
    picture = FileField(label="Upload Profile Picture", validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField(label= 'Update Account')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError ('This user is taken')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError ('This email is taken')