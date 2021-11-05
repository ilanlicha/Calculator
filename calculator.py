from flask import Flask, render_template, current_app, g, Markup, session, request
from markupsafe import escape
import sqlite3
from flask.cli import with_appcontext
import random
import math
import sqlite3
import random
import os
import click
import hashlib
from flask.helpers import flash, url_for
from sqlite3.dbapi2 import Cursor
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = b'iaqi2021'

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

@app.route("/",methods=['GET','POST'])
# temporaire, à changer une fois qu'on a la bdd
def index():
    if request.method == 'POST':
        logout()
    if 'name' in session:
        return render_template("index.html", idimage=1, page_title="Calculator - Home",
                           op_lists=Markup(make_lists(all_OP_lists)))
    return redirect(url_for('login'))


@app.route("/random")
# loads a page about a random mathematician
def rand_math():
    rand_mathematician = mathematicians[random.randint(0, len(mathematicians)-1)]
    return render_template("mathematician.html", rand_math_name=rand_mathematician.name,
                           description=rand_mathematician.description, born=rand_mathematician.born,
                           died=rand_mathematician.died, contributions=rand_mathematician.contributions,
                           page_title="Calculator - "+rand_mathematician.name)


# used for the page /random
class Mathematician:
    # all strings : name, description, born (year), died (year or period/century if the year is unknown),
    # contributions to mathematics
    def __init__(self, n, de, b, di, c):
        self.name = n
        self.description = de
        self.born = b
        self.died = di
        self.contributions = c


# dictionary used to dictate what can and what cannot be in a formula
OP_dictionary = {"+": "+", "-": "-", "x": "*", "÷": "/", "cos": "math.cos", "sin": "math.sin", "tan": "math.tan",
                 "accos": "math.acos", "arcsin": "math.asin", "arctan": "math.atan", "distance": "math.dist",
                 "cosh": "math.cosh", "sinh": "math.sinh", "tanh": "math.tanh", "arccosh": "math.acosh",
                 "arcsinh": "math.asinh", "arctanh": "math.atanh", "toDegrees": "math.degrees", "toRadians":
                 "math.radians", "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6",
                 "7": "7", "8": "8", "9": "9", "(": "(", ")": ")", " ": " "}


# lists of operations, the first item in the list is the category
OP_arithmetic = ["Arithmetic", "+", "-", "x", "÷"]
OP_trigonometric = ["Trigonometric", "cos", "sin", "tan", "arcos", "arcsin", "arctan", "distance"]
OP_hyperbolic = ["Hyperbolic", "cosh", "sinh", "tanh", "arcosh", "arcsinh", "arctanh"]
OP_conversions = ["Conversions", "toDegrees", "toRadians"]


# list   with all the lists
all_OP_lists = [OP_arithmetic, OP_trigonometric, OP_hyperbolic, OP_conversions]


def parse_formula(formula, dictionary):
    # test for unwanted functions in the formula to prevent harmful code from going through the eval
    formula_test = formula
    for key_dict in dictionary:
        formula_test = formula_test.replace(key_dict, "")
    if formula_test != "":
        return "Error, there were unwanted elements in your formula"
    for key_dict in dictionary:
        if formula.find(key_dict) != -1:
            formula = formula.replace(key_dict, dictionary[key_dict])
    return eval(formula, globals())


# function that makes the html from the list of operations
def make_lists(op_lists):
    list_code = ""
    for sublist in op_lists:
        list_code += '<h3>'+sublist[0]+'</h3>'
        list_code += '<p><select name="'+sublist[0]+'">'
        sublist.pop(0)
        sublist.insert(0, "")
        for element in sublist:
            list_code += '<option class="operation_item">'+element+'</option>'
        list_code += '</select></p>'
    return list_code


euclid = Mathematician("Euclid", 'Euclid, sometimes called Euclid of Alexandria to distinguish him from Euclid of '
                                 'Megara, was a Greek mathematician, often referred to as the "founder of geometry" '
                                 'or the "father of geometry". He was active in Alexandria during the reign of Ptolemy'
                                 ' I (323–283 BC).', "Mid-4th century BC", "Mid-3rd century BC", "His Elements is one "
                                 "of the most influential works in the history of mathematics, serving as the main"
                                 " textbook for teaching mathematics (especially geometry) from the time of "
                                 "its publication until the late 19th or early 20th century. In the Elements, "
                                 "Euclid deduced the theorems of what is now called Euclidean geometry from a "
                                 "small set of axioms. Euclid also wrote works on perspective, conic sections, "
                                 "spherical geometry, number theory, and mathematical rigor.")

pythagoras = Mathematician("Pythagoras", "Pythagoras of Samos was an ancient Ionian Greek philosopher and the "
                                         "eponymous founder of Pythagoreanism. His political and religious "
                                         "teachings were well known in Magna Graecia and influenced the "
                                         "philosophies of Plato, Aristotle, and, through them, Western philosophy.",
                           "570 BC", "495 BC", 'According to Aristotle, the Pythagoreans used mathematics for solely '
                                               'mystical reasons, devoid of practical application. They believed that '
                                               'all things were made of numbers. The number one (the monad) '
                                               'represented the origin of all things and the number two (the dyad)'
                                               ' represented matter. The number three was an "ideal number" because'
                                               ' it had a beginning, middle, and end and was the smallest number'
                                               ' of points that could be used to define a plane triangle,'
                                               ' which they revered as a symbol of the god Apollo. The number'
                                               ' four signified the four seasons and the four elements. '
                                               'The number seven was also sacred because it was the number'
                                               ' of planets and the number of strings on a lyre, and because '
                                               'Apollo\'s birthday was celebrated on the seventh day of each month.'
                                               ' They believed that odd numbers were masculine, that even numbers '
                                               'were feminine, and that the number five represented marriage, '
                                               'because it was the sum of two and three. ')


mathematicians = (euclid, pythagoras)

""" Authentication """
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['password']:
            flash("Please fill all the fields")
            return redirect(url_for('login'))
        else:
            db = get_db()
            name = request.form['name']
            password = hashlib.sha256(request.form['password'].encode("utf-8")).hexdigest()
            sql = db.cursor().execute("SELECT * FROM user WHERE name=(?) and password=(?)", (name, password))
            found = sql.fetchone()
            if found:
                session['name'] = request.form['name']
                return redirect(url_for('index'))
            else:
                flash(f"Account doesn't exists")
                return redirect(url_for('login'))
    return render_template('login.html')

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        db = get_db()
        name = request.form['name']
        password = request.form['password']
        confirm = request.form['confirm']
        if not name or not password or not confirm:
            flash("Please fill all the fields")
        else:
            sql = db.cursor().execute("SELECT * FROM user WHERE name=(?)", [name])
            found = sql.fetchone()
            if found:
                flash("User already exists")
            else:
                if not request.form['password'] == request.form['confirm']:
                    flash("Passwords not corresponding")
                else:
                    password = hashlib.sha256(request.form['password'].encode("utf-8")).hexdigest()
                    quote = request.form['quote']
                    db.execute(f"INSERT INTO user(name,password,quote) values(\"{name}\",\"{password}\",\"{quote}\")")
                    db.commit()
                    flash("Account created")
                    return redirect(url_for('login'))
        return redirect(url_for('register'))
    return render_template('register.html')

@app.route("/logout",methods=['GET','POST'])
def logout():
    session.pop('name', None)
    session.pop('password', None)
    return redirect(url_for('index'))

@app.route("/profil",methods=['POST','GET'])
def profil():
    db = get_db()
    sql = db.cursor().execute("SELECT favorite_operation FROM user WHERE name=(?)", [session['name']])
    operationFav = sql.fetchone()
    sql = db.cursor().execute("SELECT op.formule, op.calcul, op.resultat FROM operation op"
                +" INNER JOIN user us"
                +" ON op.idUser = us.ID"
                +" WHERE us.name = (?)"
                ,[session['name']])
    historiqueUser = sql.fetchall()
    sql = db.cursor().execute("SELECT quote FROM user WHERE name=(?)", [session['name']])
    quoteUser = sql.fetchone()
    return render_template('profil.html',favorit=operationFav, historyUser=historiqueUser, quote=quoteUser)
