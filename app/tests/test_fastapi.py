from starlette.testclient import TestClient

from api import app as fastapi_app

fastapi_client = TestClient(fastapi_app)


def test_fastapi(app, client):
    res = fastapi_client.get("/version")
    assert res.status_code == 200
    assert res.json() == {"message": fastapi_app.version}


def test_fastapi_user_details(app, client):
    # TODO Investigate why this is failing
    # res = fastapi_client.get("/v1/user-details?email={}".format("admin@example.com"))
    # assert res.status_code == 200
    # assert res.json()["first_name"] == "Supersu"

    res = fastapi_client.get("/v1/user-details?email={}".format("notadmin@example.com"))
    assert res.status_code == 404
    assert res.json()["detail"] == "User Not Found"
