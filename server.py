from flask import Flask, render_template, request, url_for, flash, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user, logout_user, current_user, login_required
from flask_mail import Mail, Message
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from forms import MeatForm, RegistrationForm, LoginForm, ChickenForm, FishForm,MeatForm, ContactUsForm, SearchForm, ResetRequestForm, ResetPasswordForm, AccountForm
from jinja2 import StrictUndefined
from  static import img
from smtplib import SMTP
from flask_bcrypt import Bcrypt
from model import connect_to_db, db, User, Fish, Meat, Chicken, ContactUs
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import os , secrets
from secret_key import secret_key
from random import sample
import random

app=Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@127.0.0.1:3306/SM'

from model import db, User, Fish, Meat, Chicken, ContactUs

db.init_app(app)

with app.app_context():
    db.create_all()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tno635788@gmail.com'
app.config['MAIL_PASSWORD'] = 'qgujfqjxyswrfzce'

print("1------------------------")

#db= SQLAlchemy(app)
print("2------------------------")

login_manager = LoginManager(app)
mail = Mail(app)
bcrypt=Bcrypt(app)
print("3------------------------")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



@login_manager.unauthorized_handler
def unauthorized():
   
    return redirect(url_for('Loginpage'))




@app.route("/")
@app.route("/Home.html")
def homepage():

    return render_template("Home.html")
def set_graphical_password_choices(form):
    choices = [
        ('image_1.png', 'Image 1'), ('image_2.png', 'Image 2'), ('image_3.png', 'Image 3'),
        ('image_4.png', 'Image 4'), ('image_5.png', 'Image 5'), ('image_6.png', 'Image 6'),
        ('image_7.png', 'Image 7'), ('image_8.png', 'Image 8'), ('image_9.png', 'Image 9'),
        ('image_10.png', 'Image 10'), ('image_11.png', 'Image 11'), ('image_12.png', 'Image 12'),
        ('image_13.png', 'Image 13'), ('image_14.png', 'Image 14'), ('image_15.png', 'Image 15'),
    ]
    random.shuffle(choices)
    selected_choices = choices[:15]
    form.graphical_password.choices = selected_choices
    return selected_choices

@app.route('/Registertion.html', methods=['POST','GET'])
def register_user():
    if current_user.is_authenticated:
        return redirect(url_for('accountpage'))

    form = RegistrationForm()
    choices = [
    ('image_1.png', 'Image 1'), ('image_2.png', 'Image 2'), ('image_3.png', 'Image 3'),
    ('image_4.png', 'Image 4'), ('image_5.png', 'Image 5'), ('image_6.png', 'Image 6'),
    ('image_7.png', 'Image 7'), ('image_8.png', 'Image 8'), ('image_9.png', 'Image 9'),
    ('image_10.png', 'Image 10'), ('image_11.png', 'Image 11'), ('image_12.png', 'Image 12'),
    ('image_13.png', 'Image 13'), ('image_14.png', 'Image 14'), ('image_15.png', 'Image 15'),
]


    set_graphical_password_choices(form)

    if form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        selected_images = form.graphical_password.data
        graphical_password = ','.join(selected_images)

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=encrypted_password,
            graphical_password=graphical_password
        )

        db.session.add(user)
        db.session.commit()

        flash(f'Registration successful for {form.username.data}', category='success')
        return redirect(url_for('Loginpage'))

    #flash(f'Registration unsuccessful for {form.username.data}', category='danger')
    return render_template("Registertion.html", form=form)

@app.route("/Login.html", methods=['POST','GET'])
def Loginpage():
    if current_user.is_authenticated:
        return redirect(url_for('accountpage'))

    form = LoginForm()
    choices = [
        ('image_1.png', 'Image 1'), ('image_2.png', 'Image 2'), ('image_3.png', 'Image 3'),
        ('image_4.png', 'Image 4'), ('image_5.png', 'Image 5'), ('image_6.png', 'Image 6'),
        ('image_7.png', 'Image 7'), ('image_8.png', 'Image 8'), ('image_9.png', 'Image 9'),
        ('image_10.png', 'Image 10'), ('image_11.png', 'Image 11'), ('image_12.png', 'Image 12'),
        ('image_13.png', 'Image 13'), ('image_14.png', 'Image 14'), ('image_15.png', 'Image 15'),
    ]
    set_graphical_password_choices(form)

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        graphical_password = request.form.getlist('graphical_password')

        app.logger.info(f"Email: {email}, Password: {password}, Graphical Password: {graphical_password}")

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            # Check graphical password
            stored_graphical_password = user.graphical_password.split(',')
            # Perform authentication logic based on selected images
            if set(graphical_password) == set(stored_graphical_password):
                login_user(user)
                flash(f'Login successful for {email}', category='success')
                return redirect(url_for('homepage'))
            else:
                flash('Graphical password incorrect', category='danger')
        else:
            flash(f'Login unsuccessful for {email}', category='danger')

    return render_template("Login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Loginpage'))

@app.route("/Chicken_s.html", methods=['POST','GET'])
@login_required 
def Add_Chicken():
    form = ChickenForm()
    if form.validate_on_submit():
        chicken = Chicken (prosubchicken= form.prosubchicken.data, prochicken=form.prochicken.data)
        db.session.add(chicken)
        db.session.commit()
        flash(f'Solution added successfully', category='success')
        return redirect(url_for('homepage'))
    return render_template("Chicken_s.html", form=form)
   
@app.route("/Meat_s.html", methods=['POST','GET'])
@login_required 
def Add_Meat():
    form = MeatForm()
    if form.validate_on_submit():
        meat = Meat (prosubmeat= form.prosubmeat.data, promeat=form.promeat.data)
        db.session.add(meat)
        db.session.commit()
        flash(f'Solution added successfully', category='success')
        return redirect(url_for('homepage'))
    return render_template("meat_s.html", form=form)

@app.route("/fish_s.html", methods=['POST','GET'])
@login_required 
def Add_Fish():
    form = FishForm()
    if form.validate_on_submit():
        fish = Fish (prosubfish= form.prosubfish.data, profish=form.profish.data)
        db.session.add(fish)
        db.session.commit()
        flash(f'Solution added successfully', category='success')
        return redirect(url_for('homepage'))
    return render_template("fish_s.html", form=form)

@app.route("/ContactUs.html", methods=['POST','GET'])
def ContactUspage():
    form = ContactUsForm()
    if form.validate_on_submit():
        contact = ContactUs (username= form.username.data,email=form.email.data,msg= form.msg.data )
        db.session.add(contact)
        db.session.commit()
        flash(f'Message sent successfully', category='success')
        return redirect(url_for('homepage'))
    return render_template("ContactUs.html", form=form )

@app.route("/Chicken.html", methods=['POST','GET'])
def chickenpage():
    problem = Chicken.query.all()
    return render_template("Chicken.html", problem=problem)


@app.route("/fish.html", methods=['POST','GET'])
def fishpage():
    problem = Fish.query.all()
    return render_template("fish.html", problem=problem)

@app.route("/meat.html", methods=['POST','GET'])
def meatpage():
    problem = Meat.query.all()
    return render_template("meat.html", problem=problem)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/profile_pic', picture_fn)
    form_picture.save(picture_path)

    return picture_fn

@app.route("/Account.html", methods=['POST','GET'])
@login_required 
def accountpage():
    form = AccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file= picture_file
        current_user.username= form.username.data
        current_user.email = form.email.data
        db.session.merge(current_user)
        db.session.commit()
        flash(f'updated!', 'success')
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pic/'+ current_user.image_file)  
    return render_template('Account.html', form=form,image_file=image_file)

@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@app.route('/search', methods=['POST'])
@login_required 
def search():
    form = SearchForm()
    postchicken = Chicken.query
    postfish =Fish.query
    postmeat =Meat.query

    if form.validate_on_submit():
        searched = form.searched.data
        postfish = postfish.filter(Fish.prosubfish.like('%'+ searched +'%'))
        postfish = postfish.order_by(Fish.prosubfish).all()
        
        postmeat = postmeat.filter(Meat.prosubmeat.like('%'+ searched +'%'))
        postmeat = postmeat.order_by(Meat.prosubmeat).all()
        
        postchicken = postchicken.filter(Chicken.prosubchicken.like('%'+ searched +'%'))
        postchicken = postchicken.order_by(Chicken.prosubchicken).all()
        return render_template("search.html", form=form, searched=searched, postfish=postfish, postchicken=postchicken , postmeat=postmeat)
    else:
        flash("Please enter input", "danger")
    return redirect(url_for('homepage'))

def send_mail(user):
    token = user.get_token()
    msg = Message('Password Reset Request', recipients = [user.email], sender = 'noreply@techno.com')
    msg.body = f''' To reset the password. Please follow the link below.
    {url_for('reset_token', token=token,_external=True)}
    if didn't request reset password please ignore this email
    '''
    mail.send(msg)

@app.route('/change_password.html', methods=['GET','POST'])
def reset_request():
    form = ResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_mail(user)
            flash('Reset Request sent. Check Your Email', 'success')
            return redirect(url_for('Loginpage'))
    return render_template('reset_request.html', form=form)

@app.route('/change_password/<token>', methods = ['GET','POST'])
def reset_token(token):
    user =  User.verify_token(token)
    if user is None:
        flash('that is invaled token or expired. please try again', 'warning')
        redirect(url_for('reset_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.merge(user)
        db.session.commit()
        flash('Password has been reset please login', 'success')
        return redirect(url_for('Loginpage'))
    return render_template('change_password.html',form= form)

@app.route('/admin.html', methods=['GET','POST'])
@login_required 
def admin():
    problem = ContactUs.query.all()
    users = User.query.all()
    id = current_user.id
    if id == 1:
        return render_template("admin.html", problem=problem, users=users)
    else:
        flash("You must be an admin user ", " danger")
        return redirect(url_for('Loginpage'))

@app.route('/privacy.html')
def privacy():
    return render_template('privacy.html')

@app.route('/Location.html')
def location():
    return render_template('Location.html')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="127.0.0.1", port=5001, debug=True)

