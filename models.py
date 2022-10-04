from app import db  , datetime

test_question = db.Table('test_question', 
db.Column('test_id', db.Integer, db.ForeignKey('test.id')),
db.Column('question_id', db.Integer, db.ForeignKey('question.id'))
)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    Creation_date = db.Column(db.DateTime , nullable=False, default=datetime.utcnow)
    selection_type = db.Column(db.Boolean, nullable=False , default=False)
    questions = db.relationship('Question',secondary=test_question, backref='question')

    def __repr__(self):
        return { {self.id} , {self.name} }
 

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    domain_name = db.Column(db.String(10), nullable=False)
    tests = db.relationship('Test',secondary=test_question, backref='tests')

    def __repr__(self):
        return { {self.id} , {self.name} }
