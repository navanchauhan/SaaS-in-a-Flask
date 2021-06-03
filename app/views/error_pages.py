from app import app
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    return render_template('message.html',code=404,message="Whoops! Page Not Found"), 404

@app.errorhandler(500)
def page_server_error(e):
	return render_template("message.html",code=500,message="Server Could Not Process This."), 500