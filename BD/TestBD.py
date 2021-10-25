from flask import Flask
import sqlite3

import os

import click
from flask import current_app, g
from flask.cli import with_appcontext

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        try:
            os.mkdir('instance')
        except:
            print('file already exists')
        g.db = sqlite3.connect(
            os.path.join(app.instance_path, 'flaskr.sqlite'),
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def init_db():
    db = get_db()

    with current_app.open_resource('BD.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

app.cli.add_command(init_db_command)
