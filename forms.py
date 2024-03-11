from turtle import textinput
from wtforms.widgets import CheckboxInput 
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SelectMultipleField, StringField,PasswordField, SubmitField, widgets
from wtforms.validators import DataRequired, Length, EqualTo, Email,ValidationError, Regexp
from model import User
from flask_login import login_user, logout_user, current_user, login_required
 
class RegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField(label= 'Email',validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',validators=[DataRequired(), Length(min=3, max=20)])
    confirm_password = PasswordField(label= 'confirm Password',validators=[DataRequired(), EqualTo('password')])
    graphical_password = SelectMultipleField(
        label='Select 3 Images for Graphical Password',
        choices = [
    ('image_1.png', 'Image 1'), ('image_2.png', 'Image 2'), ('image_3.png', 'Image 3'),
    ('image_4.png', 'Image 4'), ('image_5.png', 'Image 5'), ('image_6.png', 'Image 6'),
    ('image_7.png', 'Image 7'), ('image_8.png', 'Image 8'), ('image_9.png', 'Image 9'),
    ('image_10.png', 'Image 10'), ('image_11.png', 'Image 11'), ('image_12.png', 'Image 12'),
    ('image_13.png', 'Image 13'), ('image_14.png', 'Image 14'), ('image_15.png', 'Image 15'),
],
        validators=[DataRequired()],
    )
    submit = SubmitField(label= 'Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError ('This user is taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError ('This email is taken')
    
    def validate_graphical_password(self, graphical_password):
        selected_images = graphical_password.data
        # Check if exactly 3 unique images are selected
        if len(selected_images) != 3:
            raise ValidationError('Please select exactly 3 unique images for the graphical password')
    
class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField(label= 'Email',validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',validators=[DataRequired(), Length(min=3, max=20)])
    graphical_password = SelectMultipleField(
        label='Select 3 Images for Graphical Password',
        choices = [
    ('image_1.png', 'Image 1'), ('image_2.png', 'Image 2'), ('image_3.png', 'Image 3'),
    ('image_4.png', 'Image 4'), ('image_5.png', 'Image 5'), ('image_6.png', 'Image 6'),
    ('image_7.png', 'Image 7'), ('image_8.png', 'Image 8'), ('image_9.png', 'Image 9'),
    ('image_10.png', 'Image 10'), ('image_11.png', 'Image 11'), ('image_12.png', 'Image 12'),
    ('image_13.png', 'Image 13'), ('image_14.png', 'Image 14'), ('image_15.png', 'Image 15'),
],

        validators=[DataRequired()],
    )
    submit = SubmitField('Login')


class ChickenForm(FlaskForm):
    prosubchicken = StringField(label= 'Recpie Name',validators=[DataRequired(), Length(min=3, max=50)])
    prochicken = StringField(label='Recpie Details',validators=[DataRequired(), Length(min=10, max=300)])
    submit = SubmitField(label= 'Add Recpie')

class FishForm(FlaskForm):
    prosubfish = StringField(label= 'Recpie Name',validators=[DataRequired(), Length(min=3, max=50)])
    profish = StringField(label='Recpie Details',validators=[DataRequired(), Length(min=10, max=300)])
    submit = SubmitField(label= 'Add Recpie')

class MeatForm(FlaskForm):
    prosubmeat = StringField(label= 'Recpie Name',validators=[DataRequired(), Length(min=3, max=50)])
    promeat = StringField(label='Recpie Details',validators=[DataRequired(), Length(min=3, max=300)])
    submit = SubmitField(label= 'Add Recpie')   

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