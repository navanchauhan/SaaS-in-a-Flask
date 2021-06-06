from starlette.testclient import TestClient

from api import app as fastapi_app

fastapi_client = TestClient(fastapi_app)

def test_fastapi(app, client):
	res = fastapi_client.get("/version")
	assert res.status_code == 200
	assert res.json() == {"message":fastapi_app.version}	

	res = fastapi_client.get("/v1/user-details?email={}".format("notadmin@example.com"))
	print(res.json())
	assert res.status_code == 404 
	assert res.json()["detail"] == "User Not Found"	