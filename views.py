
from app import app , render_template
from models import Test , Questions

@app.route('/')
def home():
    test = [ "test1", "test2","test3","test4","test5"]
    return render_template('home.html' , tests = test)


@app.route('/test')
def test():
    test = Test.query.all()

    return render_template('test.html', title = "Test List")


@app.route('/questions')
def question():
    question = Questions.query.all()

    return render_template('question.html' , title="Questions")

