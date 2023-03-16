from random import shuffle
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os
from flask_migrate import Migrate 



UPLOAD_RESUME = 'uploads\Resumes/'
UPLOAD_PROFILE = 'uploads\ProfilePic/'
ALLOWED_EXTENSIONS = {'pdf','doc','png','jpg', 'jpeg'}


# Database configuration code.
app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
app.secret_key = b'Nan36Nut37Sha50Van65'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Nominator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER
app.config['UPLOAD_RESUME']= UPLOAD_RESUME
app.config['UPLOAD_PROFILE'] = UPLOAD_PROFILE
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = "shindenutan015@gmail.com"
app.config['MAIL_PASSWORD'] = "lfkcmcdgxgagafxs"
app.config['TESTING'] = False
mail = Mail(app)
migrate = Migrate(app, db, render_as_batch=True)



login_manager = LoginManager(app=app)
login_manager.login_view = 'auth.login_choice'
#login_manager.login_view = 'auth.login_candidate'
#login_manager.login_view = 'auth.login_company'
login_manager.init_app(app)

from models import Candidate, Company


@login_manager.user_loader
def load_user(username):
    user = Company.query.filter_by(username=username).first()
    if not user:
        user = Candidate.query.filter_by(username=username).first()
    return user



@app.route('/uploads/<path:filename>')
def uploads(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename
    )



from auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)


def shuffle_list(lst):
    shuffle(lst)
    return lst
app.jinja_env.filters['shuffle'] = shuffle_list
def _enumerate(seq):
    return enumerate(seq)

app.jinja_env.filters['enumerate'] = _enumerate

if __name__ == '__main__':
    app.debug = True
    app.run()
