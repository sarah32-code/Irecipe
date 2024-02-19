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
        choices=[],
        option_widget=widgets.CheckboxInput(),  # Use CheckboxInput for multiple selection
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
        selected_images = set(graphical_password.data)

        # Check if exactly 3 unique images are selected
        if len(selected_images) != 3:
            raise ValidationError('Please select exactly 3 unique images for the graphical password')
    
class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField(label= 'Email',validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',validators=[DataRequired(), Length(min=3, max=20)])
    graphical_password = SelectMultipleField(
        label='Select 3 Images for Graphical Password',
        choices=[],  # Will be dynamically set in the route
        validators=[DataRequired()],
    )
    submit = SubmitField('Login')


class ChickenForm(FlaskForm):
    prosubchicken = StringField(label= 'Subject',validators=[DataRequired(), Length(min=3, max=50)])
    prochicken = StringField(label='Your solution',validators=[DataRequired(), Length(min=10, max=300)])
    submit = SubmitField(label= 'Add solution')

class FishForm(FlaskForm):
    prosubfish = StringField(label= 'Subject',validators=[DataRequired(), Length(min=3, max=50)])
    profish = StringField(label='Your solution',validators=[DataRequired(), Length(min=10, max=300)])
    submit = SubmitField(label= 'Add solution')

class MeatForm(FlaskForm):
    prosubmeat = StringField(label= 'Subject',validators=[DataRequired(), Length(min=3, max=50)])
    promeat = StringField(label='Your solution',validators=[DataRequired(), Length(min=3, max=300)])
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
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8), Regexp(regex=r'.*[A-Z].*', message="Password must contain at least one uppercase letter"), Regexp(regex=r'.*[a-z].*', message="Password must contain at least one lowercase letter"), Regexp(regex=r'.*\d.*', message="Password must contain at least one digit")])
    confirm_password = PasswordField(label= 'Confirm Password',validators=[DataRequired(), EqualTo('password')])
    picture = FileField(label="Upload Profile Picture", validators=[FileAllowed(['jpg','png'])])
    graphical_password = SelectMultipleField(label='Select 3 Images for Graphical Password', choices=[], validators=[DataRequired()])
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
    
    # def validate_graphical_password(self, graphical_password):
    #     if len(graphical_password.data) != 3:
    #         raise ValidationError('Please select exactly 3 images for the graphical password')