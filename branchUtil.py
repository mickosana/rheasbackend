from Models import db

class branchutil():
    def addbranch(self,branch):
        db.session.add(branch)
        db.session.commit()
