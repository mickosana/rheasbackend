from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from marshmallow import Schema, fields, ValidationError, pre_load

app = Flask(__name__)
app.config.from_pyfile('database.config')
db = SQLAlchemy(app)

class member(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    surname=db.Column(db.String(20))
    id_number=db.Column(db.String(20))
    branch=db.Column(db.Integer,db.ForeignKey("branch.id"))
    department=db.Column(db.Integer,db.ForeignKey("department.id"))
    age=db.Column(db.Integer)
    dateregistered=db.Column(db.Date)
    membership = db.relationship("branch", backref=db.backref("members", lazy="dynamic"))
    def __init__(self,name,surname,idno,branch,department,age):
        self.name=name
        self.surname=surname
        self.age=age
        self.department=department
        self.branch=branch
        self.id_number=idno
        self.dateregistered=date.today()



class branch(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))


    def __init__(self,name):
        self.name=name


class department(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    members=db.relationship('member',backref=db.backref('dept_members'),lazy='dynamic')
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
    amount=db.Column(db.Integer)
    date=db.Column(db.Date)
    tenderedby=db.Column(db.Integer,db.ForeignKey('user.id'))
    def __init__(self,type,amount,tenderedby):
        self.type=type
        self.amount=amount
        self.tenderedby=tenderedby
        self.date=date.today()

class Income(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    type=db.Column(db.Integer,db.ForeignKey('incometypes.id'))
    amount=db.Column(db.Integer)
    member=db.Column(db.Integer,db.ForeignKey('member.id'))
    date=db.Column(db.Date)
    tenderedby=db.Column(db.Integer,db.ForeignKey('user.id'))
    def __init__(self,type,amount,member,tenderedby):
        self.type=type
        self.amount=amount
        self.member=member
        self.date=date.today()
        self.tenderedby=tenderedby


class user(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20))
    password=db.Column(db.String(200))
    details=db.Column(db.Integer,db.ForeignKey("member.id"))
    expensestendered=db.relationship('Expenses',backref='expenses',lazy='dynamic')


class BranchSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class DepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class memberSchema(Schema):
    def must_not_be_blank(self, data):
        if not data:
            raise ValidationError('data not provided')
    id=fields.Int(dump_only=True)
    id = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    id_number = fields.Str()
    branch = fields.Nested(BranchSchema,validate = must_not_be_blank)
    department = fields.Nested(DepartmentSchema ,validate= must_not_be_blank,only=["name"])
    age = fields.Int()
    dateregistered=fields.Date(format='iso')




class IncometypesSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str()
class ExpendituretypesSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str()
class userSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str()
    password=fields.Str()
    details=fields.Nested(memberSchema,many=True)



class ExpensesSchema(Schema):
    id=fields.Int(dump_only=True)
    type=fields.Nested(ExpendituretypesSchema)
    amount=fields.Int()
    date=fields.Date(format='iso')
    tenderedby=fields.Nested(userSchema)
    tenderTo=fields.Str()


class IncomeSchema(Schema):
    id=fields.Int(dump_only=False)
    type=fields.Nested(IncometypesSchema)
    amount=fields.Decimal(places=2,as_string=True)
    member=fields.Nested(memberSchema)
    date=fields.Date(format="iso")
    tenderedby=fields.Nested(userSchema)

member_schema=memberSchema()
members_schema=memberSchema(many=True)
user_schema=userSchema()
users_Schema=userSchema(many=True)
incometype_schema=IncometypesSchema()
incometypes_schema=IncometypesSchema(many=True)
income_schema=IncomeSchema()
incomes_schema=IncomeSchema(many=True)
branch_schema=BranchSchema()
branches_schema=BranchSchema(many=True)
department_Schema=DepartmentSchema()
departments_Schema=DepartmentSchema(many=True)
expenditure_Schema=ExpensesSchema()
expenditures_Schema=ExpensesSchema(many=True)







