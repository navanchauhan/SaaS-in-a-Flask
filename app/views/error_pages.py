# -*- coding: utf-8 -*-
"""
This file describes the errors and the message the user should see.
"""

from app import app
from flask import render_template


@app.route("/Simulate500")
def simulate_500():
    """
    Used to simulate a error 500 for test coverage of 500 handling
    """
    return 500


@app.errorhandler(403)
def page_forbidden(e):
    """
    Thrown when a user accesses a page with @flask_login.login_required
    """
    return (
        render_template(
            "message.html", code=403, message="Forbidden. You shall not pass"
        ),
        403,
    )


@app.errorhandler(404)
def page_not_found(e):
    """
    Page for resource or file nout found
    """
    return (
        render_template("message.html", code=404, message="Whoops! Page Not Found"),
        404,
    )


@app.errorhandler(500)
def page_server_error(e):
    """
    Page for internal server error
    """
    return (
        render_template(
            "message.html", code=500, message="Server Could Not Process This."
        ),
        500,
    )
