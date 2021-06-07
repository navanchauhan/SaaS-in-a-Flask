# -*- coding: utf-8 -*-
"""
Test(s) for Flask Views
"""
from itsdangerous.url_safe import URLSafeSerializer
from app import app as flask_app

ts = URLSafeSerializer(flask_app.config["SECRET_KEY"])
"""
To create confirmation tokens
"""

data2check_visitors = {
    "/index": {"code": 200, "data": b"Nice Tagline"},
    "/": {"code": 200, "data": b"Nice Tagline"},
    "/ContactUs": {"code": 200, "data": b"send us a message."},
    "/doesnotexists": {"code": 404, "data": b"Page Not Found"},
    "/logout": {"code": 200, "data": b"You have been logged out."},
    "/dashboard": {
        "code": 401,
        "data": b"You need to be logged in to access this resource",
    },
    "/signup": {"code": 200, "data": b"Register your account."},
    "/signin": {"code": 200, "data": b"Sign in to your account."},
    "/Simulate500": {"code": 500, "data": b"Server Could Not Process This."},
    "/admin/user/": {"code": 403, "data": b"Forbidden"},
    "/confirm": {"code": 200, "data": b"Token not provided in URL Parameter"},
    "/confirm?confirmation_token=123": {"code": 200, "data": b"Bad Token Provided"},
}
"""
Dictionary of Path, Expected Status Code and Data to Test for Visitors
"""


def test_visitors(app, client):
    """
    Test if Vistors get expected endpoints and status codes
    """
    for page in data2check_visitors:
        res = client.get(page)
        print("Testing %s", page)
        assert res.status_code == data2check_visitors[page]["code"]
        assert data2check_visitors[page]["data"] in res.data


def test_user_auth_flow(app, client):
    """
    Test User Authentication Flow

    Tests Registeration, Email-Confirmation and Log-in along with appropriate redirects.
    """
    res = client.post(
        "/signup",
        data=dict(
            email="test@example.com",
            first_name="John",
            password="testpassword",
        ),
        follow_redirects=True,
    )

    assert res.status_code == 200
    assert b"confirm your email" in res.data

    res = client.post(
        "/signin",
        data=dict(email="test@example.com", password="testpassword"),
        follow_redirects=True,
    )
    assert res.status_code == 200
    assert b"Please Confirm Your Email First." in res.data

    confirmation_token = ts.dumps("test@example.com", salt="email-confirm-key")
    res = client.get(
        "/confirm?confirmation_token={}".format(confirmation_token),
        follow_redirects=True,
    )
    print(res.data)
    assert b"Succesfully Verified" in res.data

    res = client.post(
        "/signin",
        data=dict(email="test@example.com", password="testpassword"),
        follow_redirects=True,
    )
    assert res.status_code == 200
    assert b"Hi John" in res.data

    res = client.get("/logout", follow_redirects=True)
    assert res.status_code == 200
    assert b"You have been logged out." in res.data

    res = client.post(
        "/signin",
        data=dict(email="test@example.com", password="testpassword"),
        follow_redirects=True,
    )
    assert res.status_code == 200
    assert b"Hi John" in res.data

    res = client.get("/signin", follow_redirects=True)
    assert res.status_code == 200
    assert b"Hi John" in res.data

    res = client.get("/signup", follow_redirects=True)
    assert res.status_code == 200
    assert b"Hi John" in res.data

    res = client.get("/admin/user/")
    assert res.status_code == 403

    res = client.get("/logout")
    res = client.post(
        "/signin",
        data=dict(email="testtest@example.com", password="123456"),
        follow_redirects=True,
    )
    assert res.status_code == 200
    assert b"Incorrect Email" in res.data
    res = client.post(
        "/signin",
        data=dict(email="test@example.com", password="incorrectpassword"),
        follow_redirects=True,
    )
    assert res.status_code == 200
    assert b"Incorrect Password" in res.data

    res = client.post(
        "/signup",
        data=dict(
            email="test@example.com",
            first_name="John",
            password="testpassword",
        ),
        follow_redirects=True,
    )
    assert res.status_code == 200
    assert b"Oops! An account with that email already exists" in res.data
