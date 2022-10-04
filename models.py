from app import *

class Test(db.Model):
    test_id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(255), unique=True, nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    Creation_date = db.Column(db.DateTime , nullable=False, default=datetime.utcnow)
    selection_type = db.Column(db.Boolean, nullable=False , default=False)

    def __repr__(self):
        return '<Name %r>' % self.test_id , '<Name %r>' % self.test_name


    
class Questions(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    question_name = db.Column(db.String(255), unique=True, nullable=False)
    domain_name = db.Column(db.String(10), nullable=False)
    Creation_date = db.Column(db.DateTime , nullable=False, default=datetime.utcnow)
    selection_type = db.Column(db.Boolean, nullable=False , default=False)


    def __repr__(self):
        return '<Name %r>' % self.question_id , '<Name %r>' % self.question_name
