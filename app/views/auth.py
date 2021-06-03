from app import app, db, models, login_manager
from app.forms.app_forms import UserSignUp, UserLogIn 
from flask import render_template, flash,url_for, redirect
from app.misc_func import flash_errors
import flask_login


@app.route("/signup", methods=['GET', 'POST'])
def register_user():
    form = UserSignUp()
    if form.validate_on_submit():
        user = models.User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            confirmation=False,
            password=form.password.data,
            )
        db.session.add(user)
        db.session.commit() 
    flash_errors(form)
    return render_template("auth/signup.html",form=form)

@app.route("/login", methods=['GET', 'POST'])
def signin_user():
    form = UserLogIn()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is not None:
            if user.check_password(form.password.data):
                flask_login.login_user(user)
                return redirect(url_for("user_dashboard"))
    flash_errors(form)
    return render_template("auth/signin.html",form=form) 

@flask_login.login_required
@app.route("/dashboard")
def user_dashboard():
    return render_template("dashboard.html",user=flask_login.current_user)
