
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Database configuration code.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Nominator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import views, models

login_manager = LoginManager()
login_manager.login_view = 'auth.signup'
login_manager.init_app(app)

from models import User

@login_manager.user_loader
def load_user(username):
    return User.query.get(int(username))

from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


if __name__ == '__main__':
    app.debug = True
    app.run()