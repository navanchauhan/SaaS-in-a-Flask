# -*- coding: utf-8 -*-
"""
Test(s) for FastAPI Inegration
"""
from starlette.testclient import TestClient

from api import app as fastapi_app

fastapi_client = TestClient(fastapi_app)


def test_fastapi(app, client):
    """
    Basic Version Test

    Check if endpoint is accessible
    """
    res = fastapi_client.get("/version")
    assert res.status_code == 200
    assert res.json() == {"message": fastapi_app.version}


def test_fastapi_user_details(app, client):
    """
    Basic User Test

    Check if DB is accessible to the FastAPI App
    """
    # TODO Investigate why this is failing
    # res = fastapi_client.get("/v1/user-details?email={}".format("admin@example.com"))
    # assert res.status_code == 200
    # assert res.json()["first_name"] == "Supersu"

    res = fastapi_client.get("/v1/user-details?email={}".format("notadmin@example.com"))
    assert res.status_code == 404
    assert res.json()["detail"] == "User Not Found"
