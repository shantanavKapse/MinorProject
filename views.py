import json

from flask_login import login_required

from app import app
from flask import render_template,  request, redirect, url_for
from models import Test, Question
from personality_predict import predict_personality
import random


@app.route('/')
def home():
    test = Test.query.order_by(Test.creation_date.desc()).limit(5).all()
    return render_template('home.html' , tests = test)


@app.route('/tests')
def tests():
    all_tests = Test.query.all()
    return render_template('tests.html', tests=all_tests)


@app.route('/test/<int:id>' , methods=['GET', 'POST'])
@login_required
def test_detail(id):
    test = Test.query.filter_by(id=id).first()
    if request.method=="POST":
        return redirect(url_for('personality-test'))

    return render_template('test_detail.html', test=test)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/personality-test', methods=['GET', 'POST'])
@login_required
def personality_test():
    ques_op = random.choices(Question.query.filter_by(domain_name='Openness').all(),k=2) 
    ques_nc = random.choices(Question.query.filter_by(domain_name='Neuroticism').all(),k=2) 
    ques_ev = random.choices(Question.query.filter_by(domain_name='Extraversion').all(),k=2) 
    ques_ac = random.choices(Question.query.filter_by(domain_name='Agreeableness').all(),k=2) 
    ques_cc = random.choices(Question.query.filter_by(domain_name='Conscientiousness').all(),k=2)

    if request.method == 'POST':
        data = request.form

        return redirect(url_for('answer_page', json=json.dumps(data)), code=307)

    ques_lis=[]
    [ques_lis.extend(l) for l in (ques_op,ques_nc,ques_ev,ques_ac,ques_cc)]
    random.shuffle(ques_lis)

    return render_template('questionnaire.html', list_of_question=ques_lis)


@app.route('/answer', methods=['POST'])
def answer_page():
    if request.method == 'POST':
        data = request.form

        prediction_data = {}
        for tag, ans in data.items():
            prediction_data[tag] = ans

        ans = predict_personality(prediction_data)
        print(ans)
        return render_template('answer_page.html', results=ans)
    

@app.route('/company')
def company():
    return render_template('company.html')