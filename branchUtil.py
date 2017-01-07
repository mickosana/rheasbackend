from  flask import Flask,jsonify
from flask_restful import Resource , reqparse
from Models import *

class branchResource(Resource):
    def get(self,branchname):
        parser = reqparse.RequestParser()
        parser.add_argument(branchname)
        args = parser.parse_args()
        name = args['branchid']
        branch_result = branch.query.get(name)
        br = branch_schema.dump(branch_result).data
        members_result=members_schema.dump(branch_result.members.all()).data
        response = {}
        if len(br) == 0:
            response['Error'] = "That branch does not exist"
        else:
            response = jsonify({'branch': br,'members':members_result})
        return response
class BranchlistResource(Resource):
    def get(self):
        result=branch.query.all()
        print(result)
        branches=branches_schema.dump(result).data
        print(branches)
        return (jsonify({"branches":branches}))