
from app import app, random
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


@app.route('/Personality-Test')
def personality_test():
    ques_op = random.choices(Question.query.filter_by(domain_name='openness_criteria').all(),k=2) 
    ques_nc = random.choices(Question.query.filter_by(domain_name='neuroticism_criteria').all(),k=2) 
    ques_ev = random.choices(Question.query.filter_by(domain_name='extraversion_criteria').all(),k=2) 
    ques_ac = random.choices(Question.query.filter_by(domain_name='agreeableness_criteria').all(),k=2) 
    ques_cc = random.choices(Question.query.filter_by(domain_name='conscientiousness_criteria').all(),k=2)

    ques_lis=[]
    [ques_lis.extend(l) for l in (ques_op,ques_nc,ques_ev,ques_ac,ques_cc)]
    random.shuffle(ques_lis)
    

    return render_template('test.html',list_of_question=ques_lis)
