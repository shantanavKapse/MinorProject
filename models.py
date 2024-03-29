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
    Female = 'Female'
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
    about_me = db.Column(db.String(500), nullable = True)
    profile_pic = db.Column(db.String(200) , nullable = True , default = 'default_pic.jpg')
    skills = db.relationship('Skill', secondary="candidate_skills", backref='candidate', lazy=True)


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
    questions = db.relationship('TechnicalQuestion', backref='company', lazy=True)
    tests = db.relationship('TechnicalTest' , backref='company', lazy=True)


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

class SkillRange(enum.Enum):
    Beginner = 'Beginner'
    Intermediate = 'Intermediate'
    Advanced = 'Advanced'

class Skill(db.Model):
    skill_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Candidate_skills(db.Model):
    candidate_username = db.Column(db.String(200), db.ForeignKey("candidate.username"), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey("skill.skill_id"), primary_key=True)
    level = db.Column(db.Enum(SkillRange))

    def serialize(self):
        return {"username": self.candidate_username, "skill_id": self.skill_id, "level": self.level.value}

class Personality_result(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    Extraversion = db.Column(db.Float)
    Neuroric = db.Column(db.Float)
    Agreeableness = db.Column(db.Float)
    Conscientiousness = db.Column(db.Float)
    Open_to_experience = db.Column(db.Float)
    cluster = db.Column(db.Integer)

class Difficulty(enum.Enum):
    Easy  = 'Easy'
    Moderate = 'Moderate'
    Difficult = 'Difficult'

class Question_test(db.Model):
    question_id = db.Column(db.Integer, db.ForeignKey('technical_question.id'), primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('technical_test.id'), primary_key=True)

class TechnicalQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(2000), nullable=False)
    category = db.Column(db.String(500), nullable=False)
    owner_company = db.Column(db.String(100), db.ForeignKey("company.username"))
    difficulty = db.Column(db.Enum(Difficulty))
    option1 = db.Column(db.String(2000), nullable=False)
    option2 = db.Column(db.String(2000), nullable=False)
    option3 = db.Column(db.String(2000), nullable=False)
    correctoption = db.Column(db.String(2000), nullable=False)
    is_public = db.Column(db.Boolean, nullable=False)


    def __repr__(self):
        return f'TechnicialQuestion(id={self.id}, question="{self.question}", category="{self.category}", difficulty="{self.difficulty}", owner_company="{self.owner_company}" , correctoption="{self.correctoption} , is_public="{self.is_public}")'


class TechnicalTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    owner_company = db.Column(db.String(100), db.ForeignKey("company.username"))
    duration = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    job_role = db.Column(db.String(255), nullable=False)
    is_public = db.Column(db.Boolean, nullable=False)
    questions = db.relationship('TechnicalQuestion', secondary="question_test", backref='technical_test')


    def __repr__(self):
        return f'TechnicalTest(id={self.id}, name="{self.name}", duration="{self.duration}", job_role="{self.job_role}", is_public="{self.is_public}")'

    def add_questions(self, question_ids):
        for question_id in question_ids:
            question = TechnicalQuestion.query.get(question_id)
            if question:
                self.questions.append(question)
            

class TechnicalAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_username = db.Column(db.String, db.ForeignKey('candidate.username'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('technical_question.id'), nullable=False)
    answer = db.Column(db.String(2000), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False, default=False)
    candidate = db.relationship('Candidate', backref='user_answers')
    question = db.relationship('TechnicalQuestion', backref='user_answers')