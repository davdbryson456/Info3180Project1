from app import app, allowed_exts
from flask import render_template, request, url_for, redirect, flash
from .forms import Profile
from werkzeug.utils import secure_filename
from models import User
from sqlalchemy import exc

import datetime
import os

@app.route("/")
def home():
    return render_template('home.html')
   
   
   
   
@app.route("/profile", methods=["GET", "POST"])
def profile():
    Profile = Profile()
    
    if request.method == "POST":
        if Profile.validate_on_submit():
            
            firstname = Profile.firstname.data
            lastname = Profile.lastname.data
            gender = Profile.gender.data
            email = Profile.email.data
            location = Profile.location.data
            biography = Profile.biography.data
            created = str(datetime.datetime.now()).split()[0]
                
            photo = Profile.profilepic.data
            photo_name = secure_filename(photo.filename)
                
            person = User(firstname, lastname, gender, email, location, biography, created, photo_name)
                
            db.session.add(person)
            db.session.commit()
                
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],photo_name))
                
            flash("Profile Added", "success")
            return redirect(url_for("profiles"))
            
    
        errors = form_errors(Profile)
        flash(''.join(error+" " for error in errors), "danger")
    return render_template("create_new_profile.html", Profile = Profile)








@app.route("/profiles")
def profiles():
    users = User.query.all()
    profiles = []

    for user in users:
        profiles.append({"pro_pic": user.photo, "f_name":user.firstname, "l_name": user.lastname, "gender": user.gender, "location":user.location, "id":user.id})
    
    return render_template("view_profiles.html", profiles = profiles)

@app.route('/profile/<userid>')
def inidi_profile(userid):
    user = User.query.filter_by(id=userid).first()
    
    if user is None:
        return redirect(url_for('home'))
        
    c_y = int(user.created_on.split("-")[0])
    c_m = int(user.created_on.split("-")[1])
    c_d = int(user.created_on.split("-")[2])
    
    user.created_on = format_date_joined(c_y, c_m, c_d)
    
    return render_template("profile.html", user=user)




def format_date_joined(yy,mm,dd):
    return datetime.date(yy,mm,dd).strftime("%B, %d,%Y")




def read_file(filename):
    data = ""
    
    with open(filename, "r") as stream:
        data = stream.read()
        
    return data




def form_errors(form):
    error_list =[]
    for field, errors in form.errors.items():
        for error in errors:
            error_list.append(field+": "+error)
            
    return error_list



    
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response



@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404