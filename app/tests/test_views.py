data2check_visitors = {
	"/index": {
	"code": 200, "data": b"Nice Tagline"
	},
	"/": {
	"code": 200, "data": b"Nice Tagline"
	},
	"/ContactUs":{
	"code": 200, "data": b"send us a message."
	},
	"/doesnotexists":{
	"code": 404, "data": b"Page Not Found"
	},
	"/logout":{
	"code": 200, "data": b"You have been logged out."
	},
	"/dashboard":{
	"code":401,"data":b"You need to be logged in to access this resource"
	},
	"/signup":{
	"code":200,"data":b"Register your account."
	},
	"/signin":{
	"code":200,"data":b"Sign in to your account."
	},
	"/Simulate500":{
	"code":500,"data":b"Server Could Not Process This."
	}
}

def test_visitors(app, client):
	for page in data2check_visitors:
		res = client.get(page)
		print("Testing %s",page)
		assert res.status_code == data2check_visitors[page]["code"]
		assert data2check_visitors[page]["data"] in res.data 

def test_forms(app,client):
	res = client.post("/signin",data={"email":"123"})
	assert b"This field is required." in res.data

	res = client.post("/signup",data={"email":"123"})
	assert b"This field is required." in res.data

	res = client.post("/ContactUs",data={"email":123})
	assert b"This field is required." in res.data

def test_user_auth_flow(app, client):
	res = client.post("/signup",data=dict(
		email="test@example.com",
		first_name="John",
		password="testpassword",
		), follow_redirects=True)

	assert res.status_code == 200
	assert b"Hi John" in res.data
	
	res = client.get("/logout", follow_redirects=True)
	assert res.status_code == 200
	assert b"You have been logged out." in res.data

	res = client.post("/signin",data=dict(
		email="test@example.com",
		password="testpassword"),
		follow_redirects=True)
	assert res.status_code == 200
	assert b"Hi John" in res.data

	res = client.get("/logout")
	res = client.post("/signin",data=dict(
		email="testtest@example.com",
		password="123456"),follow_redirects=True)
	assert res.status_code == 200
	assert b"Incorrect Email" in res.data
	res = client.post("/signin",data=dict(
		email="test@example.com",
		password="incorrectpassword"),
		follow_redirects = True)
	assert res.status_code == 200
	assert b"Incorrect Password" in res.data	

	res = client.post("/signup",data=dict(
		email="test@example.com",
		first_name="John",
		password="testpassword",
		), follow_redirects=True)
	assert res.status_code == 200
	assert b"Oops! An account with that email already exists" in res.data