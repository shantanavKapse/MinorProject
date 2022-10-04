from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Nominator.db'
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.debug = True
    app.run()