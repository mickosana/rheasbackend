from  flask import Flask,jsonify
from flask_restful import Resource , reqparse
from datetime import datetime
from Models import *
class incomeResource(Resource):
    def get(self):
        income_results=Income.query.all()
        incomes=incomes_schema.dump(income_results).data
        for income in incomes:
            income['amount']=float(income['amount'])


        return(jsonify({'income':incomes}))