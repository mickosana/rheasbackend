from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('database.config')
db = SQLAlchemy(app)

class member(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    surname=db.Column(db.String(20))
    id_number=db.Column(db.String(20))
    branch=db.Column(db.Integer,db.ForeignKey('branch.id'))
    department=db.Column(db.Integer,db.ForeignKey('department.id'))
    age=db.Column(db.Integer)
    def __init__(self,name,surname,idno,branch,department,age):
        self.name=name
        self.surname=surname
        self.age=age
        self.department=department
        self.branch=branch
        self.id_number=idno
class branch(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    membership=db.relationship('member', backref=db.backref('branch_members',lazy='dynamic'))
    def __init__(self,name):
        self.name=name


class department(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    members=db.relationship('member', backref=db.backref('dept_members',lazy='dynamic'))
    def __init__(self,name):
        self.name=name
class incometypes(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40))
class expendituretypes(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40))
class Expenses(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    type=db.Column(db.Integer,db.ForeignKey('expendituretypes.id'))
    amount=db.Column(db.Float)
    date=db.Column(db.DateTime)




