from app import app
from app.forms.app_forms import MyForm
from flask import render_template, flash
from app.views import auth
from app.misc_func import flash_errors
theme = "original"

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html") 

@app.route("/ContactUs", methods=['GET', 'POST'])
def contact_us():
	form = MyForm()
	if form.validate_on_submit():
		return "Wuhu"
	flash_errors(form)
	return render_template("contact.html",form=form)