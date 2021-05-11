from flask import Blueprint, render_template, request, redirect, flash, url_for, session
from .database import User, Video
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

homepage = Blueprint('homepage', __name__)

@homepage.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    # reach route via POST
    if request.method == "POST":
        username= request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username = username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("logged in correctly", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            elif not username:
                flash("must enter an username", category="error")
            elif not password:
                flash("must enter a password", category="error")        
            flash("password incorrect, try again", category="error")
        else:
            flash("username does not exist", category="error")          
    return render_template("login.html", user=current_user)

@homepage.route('/logout')
@login_required
def logout():
    """Log user out"""
    session.clear()
    logout_user()
    return redirect("/")

@homepage.route('/register', methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # ensure username is provided
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        name = request.form.get("name")
        email = request.form.get("email")

        user = User.query.filter_by(username = username).first()
        if user:
            flash("username already exist, try with another username", category="error")
        
        elif len(email) < 4:
            flash("email must be more than 3 characters", category="error")
        elif name == None:
            flash("must provide first name", category="error")    
        elif len(username) < 2:   
            flash("username must be greater than 2 characters", category="error")
        elif len(password) < 7:
            flash("password must be grater than 7 characters", category="error")
        elif password != confirm:
            flash("password don/t much", category="error")    
        else:
            new_user = User(email=email, name=name, username=username, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Hi!", category="success")
            return redirect(url_for("views.home"))

    return render_template("register.html", user=current_user)
