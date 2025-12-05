class RegisterForm(FlaskForm):
    name = StringField("Navn", validators=[InputRequired()])
    username = StringField("Brukernavn", validators=[InputRequired()])
    password = PasswordField("Passord", validators=[InputRequired()])
    submit = SubmitField("Registrer")


