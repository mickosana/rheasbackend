from flask_restful import Resource , reqparse
from flask import Flask , jsonify ,request
from Models import *


# users=[
#         {
#             "username": "micthaworm",
#             "fullname":"courage kosana"
#         },{
#             "username":"l33tmaster",
#             "fullname":"charisma kosana"
#         }
#
#
#       ]

class UserResource(Resource):
    def post(self,name):
        result=user.query.filter_by(username=name)
        pass
    def put(self,name):
        pass
    def get(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument(name)
        args = parser.parse_args()
        name = args['profile']
        result=user.query.filter_by(username=name).first()
        users=user_schema.dump(result).data
        response={}
        if len(users)==0:
            response['Error']="The User doesnt Exist %s"
        else:
            response=jsonify({'user':users})
        return response







##for multiple user requests
class UserlistResource(Resource):

    def get(self):
        # members = member.query.all()
        # results = members_schema.dump(members)
        # return (jsonify({"members": results}))
        users=user.query.all()
        print(users)
        results=users_Schema.dump(users).data

        print(results)
        return(jsonify({"users":results}))
    def put(self,oldpass,newpass):
        parser = reqparse.RequestParser()
        parser.add_argument(oldpass)
        args = parser.parse_args()
        name = args['profile']
        result = user.query.filter_by(username=name).first()
        users = user_schema.dump(result).data
        response = {}
        if len(users) == 0:
            response['Error'] = "The User doesnt Exist %s"
        else:
            response = jsonify({'user': users})
        return response
        pass
    def delete(self):
        return {
            'message':'user deleted'

        }
##for single user requests






