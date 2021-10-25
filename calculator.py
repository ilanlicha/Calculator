from flask import Flask, render_template, current_app, g, Markup
from markupsafe import escape
import sqlite3
from flask.cli import with_appcontext
import random
import math


app = Flask(__name__)

# utiliser eval
@app.route("/")
# temporaire, à changer une fois qu'on a la bdd
def index():
    return render_template("index.html", name="Test name", idimage=1, page_title="Calculator - Home",
                           op_lists=Markup(make_lists(all_OP_lists)))


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


# dictionary for the operations, used to make the conversion from the preferred displaying format of these operations to
# the format the code will be able to process
OP_dictionary = {"+": "+", "-": "-", "x": "*", "÷": "/", "cos": "cos", "sin": "sin", "tan": "tan"
                 , "arccos": "acos", "arcsin": "asin", "arctan": "atan", "distance": "dist", "cosh": "cosh",
                 "sinh": "sinh", "tanh": "tanh", "arccosh": "acosh", "arcsinh": "asinh", "arctanh": "atanh",
                 "toDegrees": "degrees", "toRadians": "radians"}


# lists of operations
OP_arithmetic = ["Arithmetic", "+", "-", "x", "÷"]
OP_trigonometric = ["Trigonometric", "cos", "sin", "tan", "arccos", "arcsin", "arctan", "distance"]
OP_hyperbolic = ["Hyperbolic", "cosh", "sinh", "tanh", "arccosh", "arcsinh", "arctanh"]
OP_conversions = ["Conversions", "toDegrees", "toRadians"]


# dictionary with all the lists
all_OP_lists = [OP_arithmetic, OP_trigonometric, OP_hyperbolic, OP_conversions]


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
