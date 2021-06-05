from app import app, db, models, login_manager, oauth
from app.forms.app_forms import UserSignUp, UserLogIn 
from flask import render_template, flash,url_for, redirect, request
from app.misc_func import flash_errors
import flask_login
from sqlalchemy.exc import IntegrityError

@app.route("/signup", methods=['GET', 'POST'])
def register_user():
    if request.method == "GET" and flask_login.current_user.is_authenticated:
            return redirect(url_for("user_dashboard"))
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
            return render_template("auth/signup.html",form=form)
        flask_login.login_user(user)
        return redirect(url_for("user_dashboard")) 
    flash_errors(form)
    return render_template("auth/signup.html",form=form)

@app.route("/signin", methods=['GET', 'POST'])
def signin_user():
    if request.method == "GET" and flask_login.current_user.is_authenticated:
            return redirect(url_for("user_dashboard"))
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

@app.route("/login/with/google")
def login_with_google():
    redirect_uri = url_for("login_with_google_auth", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route("/login/with/google/callback")
def login_with_google_auth():
    token = oauth.google.authorize_access_token()
    g_user = oauth.google.parse_id_token(token)
    print(g_user)
    if g_user["email_verified"]:
        user = models.User(
            first_name=g_user["given_name"],
            last_name=g_user["family_name"],
            email=g_user["email"],
            confirmation=True,
            login_type="google")
        db.session.add(user)
        try:
            db.session.commit()
            flask_login.login_user(user)
            return redirect(url_for("user_dashboard"))
        except IntegrityError:
            db.session.rollback()
            user = models.User.query.filter_by(email=g_user["email"]).first()
            if user.login_type == "google":
                flask_login.login_user(user)
                return redirect(url_for("user_dashboard"))
            else:
                flash("An account already exists for this email. Please use your password to log in.")
                return redirect(url_for("signin_user"))
    else:
        return render_template(
            "message.html",
            message="To use sign-in with Google, you need a verified e-mail.",
        )

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
