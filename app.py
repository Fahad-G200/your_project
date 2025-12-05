from flask import Flask, render_template, request, redirect
import mysql.connector
from forms import RegisterForm, LoginForm   # OBS: LoginForm, ikke Loginform

app = Flask(__name__)
app.secret_key = "hemmelig-nok"


def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="DIN_DB_BRUKER",
        password="DITT_PASSORD",
        database="DIN_DATABASE"
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()


    return render_template("register.html", form=form)

