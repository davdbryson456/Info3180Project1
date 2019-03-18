from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from subprocess import call


app = Flask(__name__)
app.config['SECRET_KEY'] = "SuperSecretKey"


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://info2180-project1:password123@localhost/profilebook"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

app.config['UPLOAD_FOLDER'] = './app/static/profile_pic'

#db = SQLAlchemy(app)

allowed_exts = ["jpg", "jpeg", "png"]

from app import views