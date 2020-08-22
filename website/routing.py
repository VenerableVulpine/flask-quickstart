from website import app
from website import forms
from website import models

from flask import (
    render_template,
    url_for,
    redirect,
    request
    )
    
from flask_sqlalchemy import SQLAlchemy

@app.route("/index")
def landing():
    return render_template("index.html")