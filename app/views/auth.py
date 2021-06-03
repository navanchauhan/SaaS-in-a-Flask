from app import app, db, models
from app.forms.app_forms import UserSignUp 
from flask import render_template, flash
from app.misc_func import flash_errors


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