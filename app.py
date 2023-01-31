from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

UPLOAD_RESUME = 'uploads\Resumes/'
UPLOAD_PROFILE = 'uploads\ProfilePic/'
ALLOWED_EXTENSIONS = {'pdf','doc','png','jpg', 'jpeg'}


# Database configuration code.
app = Flask(__name__)
app.secret_key = b'Nan36Nut37Sha50Van65'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Nominator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['UPLOAD_RESUME']= UPLOAD_RESUME
app.config['UPLOAD_PROFILE'] = UPLOAD_PROFILE



login_manager = LoginManager(app=app)
login_manager.login_view = 'auth.login_candidate'
login_manager.login_view = 'auth.login_company'
login_manager.init_app(app)

from models import Candidate, Company


@login_manager.user_loader
def load_user(username):
    user = Company.query.filter_by(username=username).first()
    if not user:
        user = Candidate.query.filter_by(username=username).first()
    return user


from auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.debug = True
    app.run()
