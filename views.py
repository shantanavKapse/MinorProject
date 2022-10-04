
from app import *
from models import * 

@app.route('/')
def home():
    test = [ "test1", "test2","test3","test4","test5"]
    return render_template('home.html' , tests = test)


@app.route('/test')
def test():
    return render_template('test.html', title = "Test List")


@app.route('/question')
def question():


    return render_template('question.html' , title="Questions")
