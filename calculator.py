from flask import Flask
from flask import render_template
from markupsafe import escape
import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext


@app.route("/")
# temporaire, à changer une fois qu'on a la bdd
def index():
    return render_template("index.html", name="Test name", idimage=1)