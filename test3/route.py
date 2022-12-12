from test3 import app, db
from flask import Flask, render_template, request, url_for, flash, session, redirect
from test3.forms import RegistrationForm, LoginForm, IosForm
from jinja2 import StrictUndefined
from test3.model import User
from test3.model import Ios



@app.route("/")
@app.route("/Home.html")
def homepage():

    return render_template("Home.html")


@app.route('/Registertion.html', methods=['POST','GET'])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username= form.username.data,email=form.email.data,password= form.password.data)
        db.session.add(user)
        db.session.commit()
        #flash(f'Registertion successful for{form.username.data}', category=success)
        return redirect(url_for('Loginpage'))
    return render_template("Registertion.html", form=form)


@app.route("/Login.html", methods=['POST','GET'])
def Loginpage():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if form.email.data==user.email and form.password.data==user.password:
            #flash(f'LogIn successful for{form.email.data}', category=success)
            return redirect(url_for('homepage'))
        else:
            #flash(f'LogIn unsuccessful for{form.email.data}', category=danger)
            return redirect(url_for('Loginpage'))
    return render_template("Login.html", form=form)

@app.route("/Add_Solution.html", methods=['POST','GET'])
def Add_Solutionpage():
    form = IosForm()
    if form.validate_on_submit():
        ios = Ios (prosubios= form.prosubios.data, proios=form.proios.data)
        db.session.add(ios)
        db.session.commit()
        #flash(f'Registertion successful for{form.username.data}', category=success)
        return redirect(url_for('homepage'))

    return render_template("Add_Solution.html",form=form)
 
@app.route("/ContactUs.html")
def ContactUspage():

    return render_template("ContactUs.html")

@app.route("/IOS_Page.html", methods=['POST','GET'])
def iospage():
    problem = Ios.query.all()

    return render_template("IOS_Page.html", problem=problem)

@app.route("/android.html", methods=['POST','GET'])
def androidpage():


    return render_template("android.html")





