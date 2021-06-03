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
	}
}

def test_visitors(app, client):
	for page in data2check_visitors:
		res = client.get(page)
		print("Testing %s",page)
		assert res.status_code == data2check_visitors[page]["code"]
		assert data2check_visitors[page]["data"] in res.data 