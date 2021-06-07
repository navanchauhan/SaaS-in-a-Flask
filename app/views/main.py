# -*- coding: utf-8 -*-
"""
This is the main views module.

You should import all other views into this file rather than individually importing in __init__.py
"""

from app import app
from app.forms.app_forms import MyForm
from flask import render_template, flash
from app.views import auth, error_pages, admin
from app.misc_func import flash_errors

@app.route("/")
@app.route("/index")
def index():
    """
    The view for the landing page.
    """
    return render_template("index.html")


@app.route("/ContactUs", methods=["GET", "POST"])
def contact_us():
    """
    A simple contact us form with basic validation.

    This dummy form has not been linked to any database.
    """
    form = MyForm()
    if form.validate_on_submit():
        return "Wuhu"
    flash_errors(form)
    return render_template("contact.html", form=form)
