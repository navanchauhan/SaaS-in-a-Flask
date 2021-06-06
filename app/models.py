from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from app import bcrypt, db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String(120), primary_key=True)
    confirmation = db.Column(db.Boolean)
    paid = db.Column(db.Boolean)
    role = db.Column(db.String)
    team = db.Column(db.String)
    login_type = db.Column(db.String, default="Normie")
    _password = db.Column(db.String)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.email

    def get_role(self):
        return self.role

    def get_team(self):
        return self.team

    def is_paid(self):
        return self.paid
