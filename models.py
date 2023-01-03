from app import db
from datetime import datetime
from flask_login import UserMixin


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

class User(UserMixin, db.Model):
    username = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique = True, nullable=False)

class Candidate(User):
    firstname = db.Column(db.String(100),unique = True, nullable=False)
    middlename = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    linkedin = db.Column(db.String(100))
    github = db.Column(db.String(100))
    resume = db.Column(db.BLOB)

class Company(User):
    companyname = db.Column(db.String(100),unique = True, nullable=False)
    website = db.Column(db.String(100),unique = True, nullable=False)
    desc = db.Column(db.String(10000), nullable= False)
    founder = db.Column(db.String(100))
    founded_on = db.Column(db.DateTime)