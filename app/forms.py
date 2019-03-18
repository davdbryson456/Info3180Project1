#from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,RadioField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired

class Profile(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname=StringField('Lastname', validators=[InputRequired()])
    email= StringField('Email', validators=[InputRequired()])
    location=StringField('Firstname', validators=[InputRequired()])
    biography=TextAreaField('Biography')
    gender= RadioField('Gender', choices = [('M','Male'),('F','Female')])
    profilepic = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    