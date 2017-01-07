from flask_restful import Resource , reqparse
from flask import request,jsonify
from Models import *

class ExpenselistResource(Resource):
    def get(self):
        expenses_result=Expenses.query.all()
        expenses=expenditures_Schema.dump(expenses_result).data
        print(expenses)
        return{'expenses':expenses}

