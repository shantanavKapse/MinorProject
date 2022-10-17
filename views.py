
from app import app
from flask import render_template
from models import Test , Question



@app.route('/')
def home():
    test = Test.query.order_by(Test.creation_date.desc()).limit(5).all()
    return render_template('home.html' , tests = test)


@app.route('/tests')
def tests():
    all_tests = Test.query.all()
    return render_template('tests.html', tests=all_tests)


@app.route('/test/<int:id>')
def test_detail(id):
    test = Test.query.filter_by(id=id).first()
    return render_template('test_detail.html', test=test)


@app.route('/about')
def about():
    return render_template('about.html')


"""@app.route('/Personality-Test')
def personality_test():
    ques_op = Question.query.filter_by(domain_name='openness_criteria').all() 
    ques_nc = Question.query.filter_by(domain_name='neuroticism_criteria').all() 
    ques_ev = Question.query.filter_by(domain_name='extraversion_criteria').all() 
    ques_ac = Question.query.filter_by(domain_name='agreeableness_criteria').all() 
    ques_cc = Question.query.filter_by(domain_name='conscientiousness_criteria').all()

    return render_template('test.html')"""
