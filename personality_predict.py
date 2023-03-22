import json
import math
import numpy as np
import joblib
from nltk.tokenize import word_tokenize
from app import db
from models import Skill, Candidate_skills, Candidate, TechnicalTest
from PyPDF2 import PdfReader
from sentence_transformers import CrossEncoder

personality_model = joblib.load('personality_predict.joblib')
similarity_model = CrossEncoder('cross-encoder/stsb-roberta-base')
questions = open('questions.json', 'r').read()
questions = json.loads(questions)
q_ids = list(questions['questions'].keys())

SKILLS = {skill.name.lower(): skill.skill_id for skill in Skill.query.all()}

answer_type = np.array([
    1, -1, 1, -1, 1, -1, 1, -1, 1, -1,
    1, -1, 1, -1, 1, 1, 1, 1, 1, 1,
    -1, 1, -1, 1, -1, 1, -1, 1, 1, 1,
    1, -1, 1, -1, 1, -1, 1, -1, 1, 1,
    1, -1, 1, -1, 1, -1, 1, -1, 1, 1
])


def predict_personality(data):
    init_arr = np.full((50), 3)
    indices = [q_ids.index(k) for k in data.keys()]
    init_arr[indices] = [x for x in data.values()]
    nis = (init_arr - 1) / 4

    cluster = personality_model.predict([nis])
    ans_vals = (init_arr[indices]-3)*answer_type[indices]

    ans = []

    for i in range(5):
        ind = i * 2
        ans.append(round(((sum(ans_vals[ind:ind + 2]) + 4) / 8) * 100, 1))

    ans_obj = {
        "Extraversion": ans[0],
        "Neurotic": ans[1],
        "Agreeableness": ans[2],
        "Conscientiousness": ans[3],
        "Open to experience": ans[4],
        "cluster": cluster
    }

    return ans_obj


def add_skills(username):
    pdf_loc = './uploads/Resumes/' + Candidate.query.filter_by(username=username).first().resume
    reader = PdfReader(pdf_loc)
    resume_text = ''
    for p in reader.pages:
        resume_text += (p.extract_text() + '\n')

    word_toks = set(tok for tok in word_tokenize(resume_text.lower()) if tok in SKILLS)

    for skill in word_toks:
        skill_exist = Candidate_skills.query.filter_by(candidate_username=username, skill_id=SKILLS[skill]).first()
        if not skill_exist:
            new_skill = Candidate_skills(candidate_username=username, skill_id=SKILLS[skill], level='Intermediate')
            db.session.add(new_skill)
            db.session.commit()


def check_similarity(username, tech_test_id):
    resume = Candidate.query.filter_by(username=username).first().resume
    if resume:
        pdf_loc = './uploads/Resumes/' + resume
        reader = PdfReader(pdf_loc)
        resume_text = ''
        for p in reader.pages:
            resume_text += (p.extract_text() + '\n')
        test_desc = TechnicalTest.query.filter_by(id=tech_test_id).first().job_role
        return round(similarity_model.predict([resume_text, test_desc])*100, 2)
    else:
        return None
