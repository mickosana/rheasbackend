from flask_restful import Resource , reqparse
from flask import request

data = {}
class User(Resource):

    def get(self):
        return {'message':'user returned by id'}
    def put(self,input):
        data[input]=request.form['data']
        return{
            input:data[input]
        }
    def delete(self):
        return {
            'message':'user deleted'

        }
class UserbyName(Resource):

    def get(self,name):
        parser=reqparse.RequestParser()
        parser.add_argument(name,help('could not find the name'))
        args=parser.parse_args()
        name=args['name']
        return {'message':'this returns a user by name %s'%name}
    def post(self,name):

        data[name] = request.form['data']
        return{'message':'user posted by %s'%data[name]}
    def put(self,name):
        data[name] = request.form['data']
        return {'message':'user %s edited'%data[name]}
class Userlist(Resource):
    def get(self):
        return{'users':'list will be here'}



