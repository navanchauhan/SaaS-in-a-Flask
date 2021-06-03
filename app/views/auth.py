from app import app, db, models, login_manager
from app.forms.app_forms import UserSignUp, UserLogIn 
from flask import render_template, flash,url_for, redirect
from app.misc_func import flash_errors
import flask_login
from sqlalchemy.exc import IntegrityError


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
        try:
            db.session.commit()
        except IntegrityError:
            flash("Oops! An account with that email already exists") 
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
            else:
                flash("Incorrect Password")
        else:
            flash("Incorrect Email")
    else:
        flash_errors(form)
    return render_template("auth/signin.html",form=form) 

@app.route("/dashboard")
@flask_login.login_required
def user_dashboard():
    return render_template("dashboard.html",user=flask_login.current_user)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return render_template("message.html",message="You have been logged out.")

@login_manager.unauthorized_handler
def unauthorized():
    return render_template("message.html",message="You need to be logged in to access this resource", code=401), 401 
