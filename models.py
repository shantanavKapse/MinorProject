from app import db
from datetime import datetime

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime , nullable=False, default=datetime.utcnow())
    description = db.Column(db.Text())
    job_role = db.Column(db.String(255), nullable=False)
    openness_criteria = db.Column(db.Float)
    neuroticism_criteria = db.Column(db.Float)
    extraversion_criteria = db.Column(db.Float)
    agreeableness_criteria = db.Column(db.Float)
    conscientiousness_criteria = db.Column(db.Float)
    skills_required = db.Column(db.PickleType)

    def __repr__(self):
        return f"{self.id}: {self.name}"
 

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), unique=True, nullable=False)
    domain_name = db.Column(db.String(50), nullable=False)
    tag = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.name}"

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), unique=True, nullable=False)
    location = db.Column(db.Text(),nullable=False)
    branches = db.Column(db.Text(),nullable=False)
    hire = db.Column(db.Integer,nullable=False) # number of candidates hire by this company till date 

    def __repr__(self):
        return f"{self.id}: {self.name}"