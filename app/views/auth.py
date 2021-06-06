from app import app, db, models, login_manager, oauth
from app.forms.app_forms import UserSignUp, UserLogIn
from flask import render_template, flash, url_for, redirect, request
from app.misc_func import flash_errors, send, send_async
import flask_login
from sqlalchemy.exc import IntegrityError
from itsdangerous.url_safe import URLSafeSerializer
from itsdangerous.exc import BadSignature

ts = URLSafeSerializer(app.config["SECRET_KEY"])


@app.route("/signup", methods=["GET", "POST"])
def register_user():
    if request.method == "GET" and flask_login.current_user.is_authenticated:
        return redirect(url_for("user_dashboard"))
    form = UserSignUp()
    if form.validate_on_submit():
        form.email.data = form.email.data.lower()
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
            return render_template("auth/signup.html", form=form)

        subject = "Confirm Your Email"
        confirmation_token = ts.dumps(user.email, salt="email-confirm-key")
        confirmation_url = url_for(
            "confirm_email", confirmation_token=confirmation_token, _external=True
        )
        body_html = render_template(
            "misc/email_confirm.html", confirmation_url=confirmation_url
        )
        body = render_template(
            "misc/email_confirm.txt", confirmation_url=confirmation_url
        )
        send(user.email, subject, body, body_html)

        flash("Please confirm your email before signing in..")
        return redirect(url_for("signin_user"))

    flash_errors(form)
    return render_template("auth/signup.html", form=form)


@app.route("/signin", methods=["GET", "POST"])
def signin_user():
    if request.method == "GET" and flask_login.current_user.is_authenticated:
        return redirect(url_for("user_dashboard"))
    form = UserLogIn()
    if form.validate_on_submit():
        form.email.data = form.email.data.lower()
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is not None:
            if user.login_type != "Normie":
                flash("Please Use Sign in With {}".format(user.login_type.title()))
            elif user.check_password(form.password.data):
                if user.confirmation:
                    flask_login.login_user(user)
                    return redirect(url_for("user_dashboard"))
                flash("Please Confirm Your Email First.")
            else:
                flash("Incorrect Password")
        else:
            flash("Incorrect Email")
    else:
        flash_errors(form)
    return render_template("auth/signin.html", form=form)


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
            email=g_user["email"].lower(),
            confirmation=True,
            login_type="google",
        )
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
            flash(
                "An account already exists for this email. Please use your password to log in."
            )
            return redirect(url_for("signin_user"))
    else:
        return render_template(
            "message.html",
            message="To use sign-in with Google, you need a verified e-mail.",
        )


@app.route("/confirm", methods=["GET", "POST"])
def confirm_email():
    confirmation_token = request.args.get("confirmation_token")
    try:
        email = ts.loads(confirmation_token, salt="email-confirm-key", max_age=86400)
    except TypeError:
        return render_template(
            "message.html", message="Token not provided in URL Parameter"
        )
    except BadSignature:
        return render_template("message.html", message="Bad Token Provided")
    user = models.User.query.filter_by(email=email).first()
    print(email)
    user.confirmation = True
    db.session.commit()
    flash("Email Has Been Succesfully Verified, You May Log In")
    return redirect(url_for("signin_user"))


@app.route("/dashboard")
@flask_login.login_required
def user_dashboard():
    return render_template("dashboard.html", user=flask_login.current_user)


@app.route("/logout")
def logout():
    flask_login.logout_user()
    return render_template("message.html", message="You have been logged out.")


@login_manager.unauthorized_handler
def unauthorized():
    return (
        render_template(
            "message.html",
            message="You need to be logged in to access this resource",
            code=401,
        ),
        401,
    )
