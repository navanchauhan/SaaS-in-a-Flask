# -*- coding: utf-8 -*-
"""
Test(s) for Forms

Tests the forms and their validations
"""
def test_incorrect_forms(app, client):
    """
    Simulate Invalid Forms
    """
    res = client.post("/signin", data={"email": "123"})
    assert b"This field is required." in res.data

    res = client.post("/signup", data={"email": "123"})
    assert b"This field is required." in res.data

    res = client.post("/ContactUs", data={"email": 123})
    assert b"This field is required." in res.data


def test_contactus(app, client):
    """Test Valid Form Submission""" 
    res = client.post(
        "/ContactUs",
        data={
            "name": "Test User",
            "subject": "Test Contact",
            "email": "testemail@email.com",
            "body": "Test Message",
        },
        follow_redirects=True,
    )
    assert res.status_code == 200
    assert b"Wuhu" in res.data
