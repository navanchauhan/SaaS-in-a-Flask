import pytest

from app import app as flask_app
from app import db
import tempfile
import os

@pytest.fixture
def app():
	flask_app.config['WTF_CSRF_ENABLED'] = False
	flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + tempfile.mkstemp(suffix='.db')[-1]
	db.create_all()
	yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()
