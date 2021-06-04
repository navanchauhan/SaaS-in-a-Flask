from app import app, login_manager, db
from flask import render_template, flash,url_for, redirect
import flask_login
from app.models import User

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app, name="Admin", template_mode="bootstrap4")

class ModelView(ModelView):
    def is_accessible(self):
        try:
            if flask_login.current_user.get_role() == "SUPERUSER":
                return True
            return False
        except AttributeError:
            return False

admin.add_view(ModelView(User, db.session))