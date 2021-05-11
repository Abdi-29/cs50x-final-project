import os
from flask import Blueprint, render_template, redirect, request, flash, url_for, session
from . import db
from flask_login import login_required, current_user
from .database import Video
import requests
import secrets
import re
from datetime import datetime 

from .forms import UploadForm



views = Blueprint('views', __name__)

@views.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@views.route('/')
@login_required
def home():
    videos = Video.query.order_by(Video.modified_time.desc()).all()
    return render_template("home.html", videos=videos, user=current_user)

@views.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    videos = Video.query.order_by(Video.modified_time.desc()).filter_by(
    user_id=current_user.id).all()
    form = UploadForm()    
    if request.method == "POST":  
        match = re.search(r"youtube\.com/.*v=([^&]*)", form.link.data)
        video_id_youtube = match.group(1)

        uploaded_video = Video(title=form.title.data,
                               link=form.link.data, description=form.description.data, user_id=current_user.id)

        # saving to database
        db.session.add(uploaded_video)
        db.session.commit()
        flash('Video uploaded successfully', category='success')
        return redirect(url_for('views.dashboard'))

    return render_template('dashboard.html', videos=videos, form=form, user = current_user)

@views.route('/video/view/<int:video_id>')
@login_required
def view_video(video_id):
    video = Video.query.get_or_404(video_id)

    match = re.search(r"youtube\.com/.*v=([^&]*)", video.link)
    video_id = match.group(1)

    return render_template('video.html', title=video.title, video=video, video_id=video_id, user=current_user)


@views.route('/video/edit/<int:video_id>', methods=['GET', 'POST'])
def edit_video(video_id):
    video = Video.query.get_or_404(video_id)

    if not video.user_id == current_user.id:
        flash('You are not allowed to view this page!', category='error')
        return redirect(url_for('dashboard'))

    form = UploadForm()

    if request.method == "POST":

        match = re.search(r"youtube\.com/.*v=([^&]*)", form.link.data)
        video_id_youtube = match.group(1)


        video.title = form.title.data
        video.link = form.link.data
        video.description = form.description.data
        video.modified_time = datetime.now()

        # saving to database
        db.session.commit()
        flash('Video updated successfully', category='success')
        return redirect(url_for('views.dashboard'))

    elif request.method == 'GET':
	    form.title.data = video.title
	    form.link.data = video.link
	    form.description.data = video.description

    return render_template('edit-video.html', title=video.title, form=form, video=video, video_id=video_id, user=current_user)

@views.route('/delete<int:video_id>')
@login_required
def delete(video_id):
    video_to_delete = Video.query.get_or_404(video_id)

    try:
        db.session.delete(video_to_delete)
        db.session.commit()
        return redirect(url_for("views.dashboard"))    
    except:
        return "There were a problem deleting that video"

@views.route('/history')
@login_required
def history():
    return ("<h1>Not available at the moment</h1>")        