import click
from flask import Flask
from flask_bcrypt import Bcrypt
from flask.cli import AppGroup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from app.models import User

database_cli = AppGroup("database")
@database_cli.command("create")
def create_database():
	db.create_all()
@database_cli.command("delete")
def delete_database():
	db.drop_all()	

app.cli.add_command(database_cli)


from app.views import main