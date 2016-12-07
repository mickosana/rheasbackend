from flask import Flask
from  flask_restful import Api
from Users import UserbyName,User,Userlist
from Models import db

app=Flask(__name__)
api=Api(app)
api.add_resource(User, '/users/', endpoint="users")
api.add_resource(UserbyName,'/users/<string:name>',endpoint="users/name")
api.add_resource(Userlist,'/users/',endpoint="users/userlist")



if __name__=="__main__":
    db.create_all()
    app.run()