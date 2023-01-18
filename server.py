from flask import Flask, render_template, request, url_for, flash, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user, logout_user, current_user, login_required
from flask_mail import Mail, Message
from forms import RegistrationForm, LoginForm, IosForm, AndroidForm, ContactUsForm, SearchForm, ResetRequestForm, ResetPasswordForm, AccountForm
from jinja2 import StrictUndefined

from smtplib import SMTP
from flask_bcrypt import Bcrypt
from model import connect_to_db,User, Ios, Android, ContactUs,db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import os , secrets
from secret_key import secret_key

app=Flask(__name__)

#app.config['SECRET_KEY']='this is techno db'
app.secret_key=secret_key

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/user.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://techno:123456@localhost:5433/technoapp'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



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


@app.route('/Registertion.html', methods=['POST','GET'])
def register_user():
    if current_user.is_authenticated:
        return redirect(url_for('accountpage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        encrypted_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username= form.username.data,email=form.email.data,password=encrypted_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Registertion successful for {form.username.data}', category='success')
        return redirect(url_for('Loginpage'))

    return render_template("Registertion.html", form=form)

@app.route("/Login.html", methods=['POST','GET'])
def Loginpage():
    if current_user.is_authenticated:
        return redirect(url_for('accountpage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash(f'LogIn successful for {form.email.data}', category='success')
            return redirect(url_for('homepage'))
        else:
            flash(f'LogIn unsuccessful for {form.email.data}', category='danger')
            #return redirect(url_for('Loginpage'))
    return render_template("Login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Loginpage'))

@app.route("/Add_Solution.html", methods=['POST','GET'])
@login_required 
def Add_Solutionpage():
    form = IosForm()
    if form.validate_on_submit():
        ios = Ios (prosubios= form.prosubios.data, proios=form.proios.data)
        db.session.add(ios)
        db.session.commit()
        flash(f'Solution added successfully', category='success')
        return redirect(url_for('homepage'))
    return render_template("Add_Solution.html", form=form)
    
@app.route("/android_s.html", methods=['POST','GET'])
@login_required 
def Add_Solutionpages():
    form = AndroidForm()
    if form.validate_on_submit():
        android = Android (prosubandroid= form.prosubandroid.data, proandroid=form.proandroid.data)
        db.session.add(android)
        db.session.commit()
        flash(f'Solution added successfully', category='success')
        return redirect(url_for('homepage'))
    return render_template("android_s.html", form=form)

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

@app.route("/IOS_Page.html", methods=['POST','GET'])
def iospage():
    problem = Ios.query.all()

    return render_template("IOS_Page.html", problem=problem)

@app.route("/android.html", methods=['POST','GET'])
def androidpage():
    problem = Android.query.all()


    return render_template("android.html", problem=problem)

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
        flash('updated!', 'success')
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pic/'+ current_user.image_file)  
    return render_template('Account.html', form=form,image_file=image_file)
    # form = AccountForm()

    # if form.validate_on_submit():
    #     

    #     if form.picture.data:
    #          image_file=save_image(form.picture.data)
    #          current_user.image_file = image_file
    #     current_user.username = form.username.data
    #     current_user.email = form.email.data
    #     #db.session.merge(User)
    #     db.session.commit()
    #     return redirect(url_for('accountpage'))
    # if request.method == "GET":
    #     form.username.data = current_user.username
    #     form.email.data = current_user.email

    # image_file = url_for('static', filename='profile_pic/'+current_user.image_file)
    # return render_template("Account.html", form=form, image_file=image_file)

@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@app.route('/search', methods=['POST'])
@login_required 
def search():
    form = SearchForm()
    postios = Ios.query
    postandroid =Android.query
    if form.validate_on_submit():
        searched = form.searched.data
        postios = postios.filter(Ios.prosubios.like('%'+ searched +'%'))
        postios = postios.order_by(Ios.prosubios).all()
        postandroid = postandroid.filter(Android.prosubandroid.like('%'+ searched +'%'))
        postandroid = postandroid.order_by(Android.prosubandroid).all()
        return render_template("search.html", form=form, searched=searched, postios=postios, postandroid=postandroid)
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
# @app.route('/change_password.html')
# def update():
#     render_template('change_password.html')

if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True)
    connect_to_db(app)
    app.run(host="127.0.0.1", port=5001, debug=True)
