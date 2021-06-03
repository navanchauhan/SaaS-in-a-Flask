from app import app
from app.forms.app_forms import MyForm
from flask import render_template, flash

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

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')