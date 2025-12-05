from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

   
    if form.validate_on_submit():
        navn = form.name.data
        brukernavn = form.username.data
        passord = form.password.data

