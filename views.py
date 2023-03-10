import json
import os

from flask_login import login_required, current_user

import models
from app import app , db
from flask import render_template,  request, redirect, send_from_directory, url_for , flash
from models import TechnicalQuestion, Test, Question, Company, Candidate , Candidate_skills , Skill , Personality_result , TechnicalTest
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
    return render_template('about.html')


@app.route('/personality-test/', methods=['GET', 'POST'])
@login_required
def personality_test():
    ques_op = random.choices(Question.query.filter_by(domain_name='Openness').all(),k=2) 
    ques_nc = random.choices(Question.query.filter_by(domain_name='Neuroticism').all(),k=2) 
    ques_ev = random.choices(Question.query.filter_by(domain_name='Extraversion').all(),k=2) 
    ques_ac = random.choices(Question.query.filter_by(domain_name='Agreeableness').all(),k=2) 
    ques_cc = random.choices(Question.query.filter_by(domain_name='Conscientiousness').all(),k=2)

    if request.method == 'POST':
        data = request.form

        prediction_data = {}
        for tag, ans in data.items():
            prediction_data[tag] = ans

        ans = predict_personality(prediction_data)

        print(ans)
        extraversion = ans['Extraversion']
        neuroticism = ans['Neurotic']
        agreeableness = ans['Agreeableness']
        conscientiousness = ans['Conscientiousness']
        openness_to_experience = ans['Open to experience']
        cluster = ans['cluster']
        #print(extraversion , neuroticism , agreeableness , conscientiousness , openness_to_experience , cluster)
        #print(current_user.username)
        test_result = Personality_result(username = current_user.username , Extraversion = extraversion , Neuroric = neuroticism , Agreeableness = agreeableness , Conscientiousness = conscientiousness , Open_to_experience = openness_to_experience , cluster = cluster)

        db.session.add(test_result)
        db.session.commit()

        return redirect(url_for('Candidate_profile' , username = current_user.username))
        #return redirect(url_for('answer_page', json=json.dumps(data)), code=307)

    ques_lis=[]
    [ques_lis.extend(l) for l in (ques_op,ques_nc,ques_ev,ques_ac,ques_cc)]
    random.shuffle(ques_lis)

    return render_template('questionnaire.html', list_of_question=ques_lis)

"""
@app.route('/answer', methods=['GET' , 'POST'])
def answer_page():
    if request.method == 'POST':
        data = request.form

        prediction_data = {}
        for tag, ans in data.items():
            prediction_data[tag] = ans

        ans = predict_personality(prediction_data)
        print(ans)
        return render_template('answer_page.html', results=ans)
"""
   

@app.route('/company')
def company():
    company = Company.query.all()
    return render_template('company.html' , company = company)


@app.route('/Candidate-Profile/<username>', methods =['GET' , 'POST'])
@login_required
def Candidate_profile(username):
    if request.method=='GET':
        results = Personality_result.query.filter_by(username=username).first()
        if results:
            labels = ['Extraversion', 'Neuroticism', 'Agreeableness', 'Conscientiousness', 'Openness']
            data = [results.Extraversion, results.Neuroric, results.Agreeableness, results.Conscientiousness, results.Open_to_experience]
        else:
            labels = None
            data = None        

        candidate = Candidate.query.filter_by(username=username).first()
        skills = []
        for skill in candidate.skills:
            print(skills)
            l = Candidate_skills.query.filter_by(candidate_username=candidate.username, skill_id= skill.skill_id).first()
            skills.append({"name": skill.name, "level": l.level.value})
        if candidate:
            if candidate.profile_pic:
                profile_pic = (candidate.profile_pic)
                
            else:
                profile_pic = None
            return render_template('Candidate_profile.html', candidate=candidate, profile_pic=profile_pic , skills=skills , labels=labels , data=data, results=results)
        else:
            return 'Candidate not found' , 404
        
    return render_template('Candidate_profile.html', candidate=candidate, profile_pic=profile_pic, skills=skills , labels=labels , data=data , results=results)


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
                candidate.profile_pic = profile_pic.filename

            resume = request.files.get('resume')
            if resume :
                os.remove(os.path.join(app.config["UPLOAD_RESUME"] , candidate.resume))
                resume.save(os.path.join(app.config["UPLOAD_RESUME"] ,resume.filename))
                candidate.resume=resume.filename
            
            candidate.username= request.form.get('username')
            candidate.email= request.form.get('email')
            candidate.firstname=request.form.get('firstname')
            candidate.lastname=request.form.get('lastname')
            candidate.linkedin=request.form.get('linkedin')
            candidate.github=request.form.get('github')
            
            db.session.commit()

            skill_name = request.form.get('skill_name')
            skill_level = request.form.get('skill_level')
  
            # find skill in database or create new skill
            skill = Skill.query.filter_by(name=skill_name).first()
            if not skill:
                skill = Skill(name=skill_name)
                db.session.add(skill)
                db.session.commit()

            # add skill to candidate
            candidate_skill = Candidate_skills( candidate_username=username, skill_id=skill.skill_id, level=skill_level )
            db.session.add(candidate_skill)
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


@app.route('/create-test/<test_id>', defaults = {'test_id': None} , methods=['GET', 'POST'])
@login_required
def create_test(test_id):
    if not test_id:
        company = Company.query.filter_by(username=current_user.username).first()
        public_question = TechnicalQuestion.query.filter_by(is_public=True , owner_company=current_user.username).all()
        if request.method == 'POST':
            testname = request.form['Testname']
            duration = request.form['duration']
            job_description = request.form['job_description']
            job_role = request.form['job_role']
            is_public = 'ispublic' in request.form
            question_ids = request.form.getlist('questions')

            new_test = TechnicalTest(
            name=testname,
            description = job_description,
            duration=duration,
            job_role=job_role,
            is_public=is_public
            )

            db.session.add(new_test)
            db.session.commit()

            new_test.add_questions(question_ids=question_ids)
            db.session.commit()
            
            flash('Test created successfully!', 'success')
            return redirect(url_for('Company_profile', username=company.username))


    return render_template ('createtest.html',company=company, public_question=public_question)


@app.route('/add-question', methods=['GET', 'POST'])
@login_required
def add_question():
    company = Company.query.filter_by(username=current_user.username).first()
    if request.method=='POST':    
        difficulty = request.form['QuDifficulty']
        question = request.form['question']
        category = request.form['category']
        option1 = request.form['option1']
        option2 = request.form['option2']
        option3 = request.form['option3']
        correct_option = request.form['correctoption']
        is_public = 'ispublic' in request.form


        new_question = TechnicalQuestion( question=question, 
            category=category,
            difficulty = difficulty,
            owner_company = current_user.username ,
            option1=option1,
            option2=option2,
            option3=option3,
            correctoption=correct_option,
            is_public=is_public
        )

        db.session.add(new_question)
        db.session.commit()
        flash('Question created successfully!', 'success')
        return redirect(url_for('Company_profile', username=company.username))


    return render_template ('addquestion.html',company=company)