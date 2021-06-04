from app import database_cli

def test_admin(app, client):
	runner = app.test_cli_runner()
	assert runner.invoke(database_cli,["admin-create"]).exit_code == 0

	res = client.post("/signin",data=dict(
		email=app.config["ADMIN_EMAIL"],
		password=app.config["ADMIN_PASSWORD"]),follow_redirects=True)

	print(res.data)
	assert b"Supersu" in res.data
	res = client.get("/admin/user/")
	assert res.status_code == 200