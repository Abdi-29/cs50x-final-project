from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, TextAreaField

from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email

class UploadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()], render_kw={'placeholder':"https://www.youtube.com/watch?v="})
    description = TextAreaField('Description')
    submit = SubmitField('Submit')

