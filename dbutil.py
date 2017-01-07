from Models import db

class DButil():
    def addrecord(self,record):
        db.session.add(record)
        db.session.commit()
    def getrecordby_id(self,_tablename,id):
       dbobj = _tablename.db.query.filter_by(id=id).first()
       db.session.delete(dbobj)
       db.session.commit()
    def getrecords(self,_tablename):
        _tablename.query.all()






