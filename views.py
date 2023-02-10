import json
import os

from flask_login import login_required, current_user

import models
from app import app , db
from flask import render_template,  request, redirect, send_from_directory, url_for , flash
from models import Test, Question, Company, Candidate
from personality_predict import predict_personality
import random


@app.route('/')
def home():
    if current_user.__class__ == models.Company:
        user_class = 'company'
    elif current_user.__class__ == models.Candidate:
        user_class = 'candidate'
    else:
        user_class = 'anonymous'
    print(user_class)
    test = Test.query.order_by(Test.creation_date.desc()).limit(5).all()
    
    
        
    return render_template('home.html', tests=test, user_class=user_class, current_user=current_user)


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
    if current_user.__class__ == models.Company:
        user_class = 'company'
    elif current_user.__class__ == models.Candidate:
        user_class = 'candidate'
    else:
        user_class = 'anonymous'
    
    return render_template('about.html' , user_class=user_class)


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


@app.route('/Candidate-Profile/<username>', methods =['GET' , 'POST'])
@login_required
def Candidate_profile(username):
    if request.method=='GET':
        candidate = Candidate.query.filter_by(username=username).first()
    
        if candidate:
            if candidate.profile_pic:
                profile_pic = (candidate.profile_pic)
                
            else:
                profile_pic = None
            return render_template('Candidate_profile.html', candidate=candidate, profile_pic=profile_pic)
        else:
            return 'Candidate not found' , 404
    
        
    return render_template('Candidate_profile.html', candidate=candidate, profile_pic=profile_pic)


@app.route('/Company-Profile/<username>', methods =['GET'])
@login_required
def Company_profile(username):
    if request.method=='GET':
        company = Company.query.filter_by(username=username).first()

        if company:
            if company.company_logo:
                company_logo = (company.company_logo)
            else:
                company_logo = None
            return render_template('Company_profile.html',company=company , company_logo=company_logo)
        else:
            return 'Company not found' , 404

    return render_template('Candidate_profile.html', company=company, company_logo=company_logo)




@app.route('/edit-profile/<username>' , methods=['GET' , 'POST'])
@login_required
def editprofile(username):
    if request.method =='GET':
        candidate = Candidate.query.filter_by(username=username).first()
        return render_template('editprofile.html' , candidate=candidate)

    if request.method == 'POST':
        old_username = request.form.get('oldusername')
        candidate = Candidate.query.filter_by(username=old_username).first()
        print(candidate)
        if candidate:
            profile_pic = request.files.get('profile_pic')
            if profile_pic:
                os.remove(os.path.join(app.config["UPLOAD_PROFILE"], candidate.profile_pic))
                profile_pic.save(os.path.join(app.config["UPLOAD_PROFILE"], profile_pic.filename))

            resume = request.files.get('resume')
            if resume :
                os.remove(os.path.join(app.config["UPLOAD_RESUME"] , candidate.resume))
                resume.save(os.path.join(app.config["UPLOAD_RESUME"] ,resume.filename))
            

            candidate.profile_pic = profile_pic.filename
            candidate.username= request.form.get('username')
            candidate.email= request.form.get('email')
            candidate.firstname=request.form.get('firstname')
            candidate.lastname=request.form.get('lastname')
            candidate.linkedin=request.form.get('linkedin')
            candidate.github=request.form.get('github')
            candidate.resume=resume.filename
            db.session.commit()

        flash(f"profile updated succefully",'success')
        return redirect(url_for('Candidate_profile', username=username , candidate=candidate))

    return render_template('editprofile.html' , candidate=candidate)



@app.context_processor
def profile_pic():
    if current_user.__class__ == models.Company:
        user_class = 'company'
    elif current_user.__class__ == models.Candidate:
        user_class = 'candidate'
    else:
        user_class = 'anonymous'
    
    if current_user.__class__ == models.Candidate:
        # Retrieve the profile picture data from the database
        user = Candidate.query.filter_by(username=current_user.username).first()
        if user.profile_pic:
            profile_pic = (user.profile_pic)
        else:
            profile_pic = None
    else:
        profile_pic = None

    if current_user.__class__ == models.Company:
        # Retrieve the profile picture data from the database
        user = Company.query.filter_by(username=current_user.username).first()
        if user.company_logo:
            company_logo = (user.company_logo)
        else:
            company_logo = None
    else:
        company_logo = None
    
    
    return dict( user_class=user_class , profile_pic=profile_pic, company_logo=company_logo)


