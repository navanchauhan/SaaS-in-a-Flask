import click
from flask import Flask
from flask_bcrypt import Bcrypt
from flask.cli import AppGroup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

	def __repr__(self):
		return '<User %r>' % self.username

database_cli = AppGroup("database")
@database_cli.command("create")
def create_database():
	db.create_all()
@database_cli.command("delete")
def delete_database():
	db.drop_all()	

app.cli.add_command(database_cli)


from app.views import main