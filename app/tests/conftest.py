# -*- coding: utf-8 -*-
"""
Configuration with basic fixtures
"""
import pytest

from app import app as flask_app
from app import db
import tempfile
import os


@pytest.fixture
def app():
    """
    Special configurations for tests

    We use a dummy database and initialise it.
    """
    flask_app.config["WTF_CSRF_ENABLED"] = False
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///" + tempfile.mkstemp(suffix=".db")[-1]
    )
    flask_app.config["MAIL_BACKEND"] = "file"  # "locmem"
    flask_app.config["MAIL_FILE_PATH"] = "/tmp/app-messages"
    db.create_all()
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
