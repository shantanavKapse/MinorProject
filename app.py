from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    tests = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5']
    return render_template('home.html', tests=tests, heading="Tests")


if __name__ == '__main__':
    app.debug = True
    app.run()