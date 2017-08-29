from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class SignInForm(FlaskForm):
    email = StringField('Email Field', [Email(), DataRequired(message='Must provide an email.')])
    name = StringField('Name Field', [DataRequired(message='Must provide a name')])