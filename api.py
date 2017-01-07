from flask import Flask
from  flask_restful import Api
from usersUtil import UserlistResource,UserResource
from membersUtil import memberResource,memberlistResource
from branchUtil import branchResource,BranchlistResource
from expensesUtil import ExpenselistResource
from incomeUtil import incomeResource
from Models import db


app=Flask(__name__)
api=Api(app)
api.add_resource(UserlistResource, '/users/all')#/users
api.add_resource(UserResource,'/users/<string:name>')#users/name
api.add_resource(memberlistResource,'/members/all')
api.add_resource(memberResource,'/members/<string:id>')
api.add_resource(BranchlistResource,'/branches/all')
api.add_resource(branchResource,'/branches/<string:branchname>')
api.add_resource(ExpenselistResource,'/expenses')
api.add_resource(incomeResource,'/incomes')


if __name__=="__main__":
    db.create_all()
    app.run()