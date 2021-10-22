from flask import Flask
from flask import render_template
from markupsafe import escape
import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext
import random


@app.route("/")
# temporaire, à changer une fois qu'on a la bdd
def index():
    return render_template("index.html", name="Test name", idimage=1)


@app.route("/random")
# loads a page about a random mathematician 
def rand_math():
    rand_mathematician = mathematicians(random.randint(0, len(mathematicians)))
    return "en cours"


class Mathematician:
    # all strings : name, description, born (year), died (year or period/century if the year is unknown),
    # contributions to mathematics
    def __init__(self, n, de, b, di, c):
        self.name = n
        self.description = de
        self.born = b
        self.died = di
        self.contributions = c


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