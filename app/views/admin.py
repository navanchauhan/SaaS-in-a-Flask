# -*- coding: utf-8 -*-
"""
SuperUser/Admin portal using flask-admin
"""
from app import app, login_manager, db
from flask import render_template, flash, url_for, redirect
import flask_login
from app.models import User

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app, name="Admin", template_mode="bootstrap4")
"""
Initialised Admin Portal
"""


class ModelView(ModelView):  # skipcq: PYL-E0102
    """
    Our extended ModelView Class

    Refer to Flask-Admin Docs for more details

    https://flask-admin.readthedocs.io/en/latest/introduction/?highlight=ModelView#modelview-configuration-attributes
    """

    def is_accessible(self):
        """This function checks if a user should be given access or not"""
        try:
            if flask_login.current_user.get_role() == "SUPERUSER":
                return True
            return False
        except AttributeError:
            return False


admin.add_view(ModelView(User, db.session))
