from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database configuration code.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Nominator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import views, models


if __name__ == '__main__':
    app.debug = True
    app.run()