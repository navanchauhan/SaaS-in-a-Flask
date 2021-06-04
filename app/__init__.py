import click
from flask import Flask
from flask_bcrypt import Bcrypt
from flask.cli import AppGroup
from flask_sqlalchemy import SQLAlchemy
import flask_login

app = Flask(__name__)
app.config.from_object('app.config')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = flask_login.LoginManager()

login_manager.init_app(app)

from app.models import User

database_cli = AppGroup("database")
@database_cli.command("create")
def create_database():
	db.create_all()
@database_cli.command("delete")
def delete_database():
	db.drop_all()
@database_cli.command("admin-create")
def make_superuser_database():
	user = User(
		first_name="Supersu",
		email=app.config["ADMIN_EMAIL"],
		password=app.config["ADMIN_PASSWORD"],
		role="SUPERUSER")
	db.session.add(user)
	db.session.commit()	

app.cli.add_command(database_cli)

from app.views import main

@login_manager.user_loader
def load_user(email):
    return User.query.filter(User.email == email).first()