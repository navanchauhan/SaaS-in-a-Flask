# -*- coding: utf-8 -*-
"""
Test(s) for Database Models
"""
from app.models import User


def test_usermodel(app, client):
    """
    Test User Model
    """
    user = User(first_name="John", email="test@example.com", password="pass")
    assert user.full_name == "John None"
    assert user.get_role() is None
    assert user.get_team() is None
    assert user.is_paid() is None
