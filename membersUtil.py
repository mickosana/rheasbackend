from  flask import Flask,jsonify
from flask_restful import Resource , reqparse
from Models import *
from toolbox import queryhelper




class memberlistResource(Resource):

    def get(self):
        qh=queryhelper()
        members=member.query.all()
        results = members_schema.dump(members).data
        for i in range(len(members)):
            br=qh.getbranchformember(members[i])
            dpt=qh.getdepart4member(members[i])
            print(br)
            print(results)
            print(dpt)
            results[i]['branch']=br['name']
            results[i]['department']=dpt['name']


        return (jsonify({"members":results}))
class memberResource(Resource):
    def get(self,id):
        qh=queryhelper()

        parser = reqparse.RequestParser()
        parser.add_argument(id)
        args = parser.parse_args()
        id= args['id']
        member_result = member.query.get(id)

        dpt=qh.getdepart4member(member_result)
        br=qh.getbranchformember(member_result)

        mem = member_schema.dump(member_result).data
        mem['department']=dpt['name']
        mem['branch']=br['name']
        response = {}
        if len(mem) == 0:
            response['Error'] = "The member  doesnt Exist %s"
        else:
            response = jsonify({'member': mem})
        return response





