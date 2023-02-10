from itsdangerous import TimedSerializer
from app import db
from datetime import datetime
import time
from flask_login import UserMixin
import enum 
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
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
    tag = db.Column(db.String(10), nullable=True)

    def __repr__(self):
        return f"{self.id}: {self.name}"

# class User(db.Model, UserMixin):
#     username = db.Column(db.String(100), primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100), unique = True, nullable=False)
#
#     def __repr__(self):
#         return f"{self.username}: {self.email}"

class CandidateGender(enum.Enum):
    Female  = 'Female'
    Male = 'Male'
    Other = 'Other'

class Candidate(db.Model, UserMixin):
    username = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100))
    linkedin = db.Column(db.String(100))
    github = db.Column(db.String(100))
    resume = db.Column(db.String(200), default=False)
    gender = db.Column(db.Enum(CandidateGender))
    profile_pic = db.Column(db.String(200) , nullable = True , default = 'default_pic.jpg')

    def __repr__(self):
        return f"Candidate: {self.username}"

    def get_id(self):
        return self.username
    
    def set_password(self, password, commit=False):
        self.password = generate_password_hash(password)

        if commit:
            db.session.commit()

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def get_reset_token(self):
        s = TimedSerializer(current_app.secret_key, 'confirmation')
        return s.dumps(self.username)
    
    def verify_reset_token(self, token, max_age=3600):
        s = TimedSerializer(current_app.secret_key, 'confirmation')
        return s.loads(token, max_age=max_age) == self.username   

    @staticmethod
    def verify_email(email):

        user = Candidate.query.filter_by(email=email).first()

        return user


class Company(db.Model, UserMixin):
    username = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    company_name = db.Column(db.String(100), unique=True, nullable=False)
    website = db.Column(db.String(100), unique=True, nullable=False)
    desc = db.Column(db.String(10000), nullable=False)
    founder = db.Column(db.String(100), nullable=False)
    founded_on = db.Column(db.DateTime, nullable=False)
    company_logo = db.Column(db.String(200) , nullable = False)

    def __repr__(self):
        return f"Company: {self.username}"

    def get_id(self):
        return self.username
    
    def set_password(self, password, commit=False):
        self.password = generate_password_hash(password)

        if commit:
            db.session.commit()

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def get_reset_token(self):
        s = TimedSerializer(current_app.secret_key, 'confirmation')
        return s.dumps(self.username)
    
    def verify_reset_token(self, token, max_age=3600):
        s = TimedSerializer(current_app.secret_key, 'confirmation')
        return s.loads(token, max_age=max_age) == self.username    
    
    @staticmethod
    def verify_email(email):

        user = Company.query.filter_by(email=email).first()

        return user