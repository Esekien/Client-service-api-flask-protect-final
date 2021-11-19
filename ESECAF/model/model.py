from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp
import sys
sys.path.append(".")
from ESECAF import db

class Population(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    municipality = db.Column(db.Text, nullable=False)
    tn = db.Column(db.Integer, nullable=False)
    tm = db.Column(db.Integer, nullable=False)
    family = db.relationship('Family', backref='population', lazy=True)
    def __init__(self, name, state,municipality,tn,tm):
        self.name = name
        self.state = state
        self.municipality = municipality
        self.tn = tn
        self.tm = tm

class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    head_of_household = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    number_of_children = db.Column(db.Integer, nullable=False)
    donations = db.Column(db.Float, nullable=False)
    population_id = db.Column(db.Integer, db.ForeignKey('population.id'),nullable=False)
    def __init__(self, head_of_household, address,cp,number_of_children,donations,population_id):
        self.head_of_household = head_of_household
        self.address = address
        self.cp = cp
        self.number_of_children = number_of_children
        self.donations = donations
        self.population_id = population_id




db.create_all()