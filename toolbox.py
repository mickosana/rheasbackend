from Models import branch_schema, department_Schema, branch, department


class queryhelper():
    def __init__(self):
        pass
    def getbranchformember(self,model):
        branch_result = branch.query.get(model.branch)
        br = branch_schema.dump(branch_result).data
        print(br)
        return br
    def getdepart4member(self,model):
       department_result = department.query.get(model.department)
       dpt = department_Schema.dump(department_result).data
       return dpt
