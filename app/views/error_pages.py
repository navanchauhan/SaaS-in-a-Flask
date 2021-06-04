from app import app
from flask import render_template

@app.route("/Simulate500")
def simulate_500():
	return 500

@app.errorhandler(403)
def page_forbidden(e):
	return render_template("message.html",code=403,message="Forbidden. You shall not pass"), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('message.html',code=404,message="Whoops! Page Not Found"), 404

@app.errorhandler(500)
def page_server_error(e):
	return render_template("message.html",code=500,message="Server Could Not Process This."), 500