from threading import Thread
from flask import flash
from flask_mailman import EmailMultiAlternatives
from app import app, mail


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                u"Error in the %s field - %s"
                % (getattr(form, field).label.text, error),
                "danger",
            )


# Sauce: https://github.com/alectrocute/flaskSaaS/blob/master/app/toolbox/email.py


def send(to, subject, body, body_html, thread=True):
    sender = app.config["MAIL_FROM"]
    message = EmailMultiAlternatives(subject, body, sender, [to])
    message.attach_alternative(body_html, "text/html")
    thr = Thread(target=send_async, args=[app, message])
    thr.start()


def send_async(app, message):
    with app.app_context():
        message.send()