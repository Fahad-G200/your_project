from flask import Flask, render_template, request, redirect
import mysql.connector
from form import RegisterForm, LoginForm   

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
    
    if form.validate_on_submit():
        navn = form.navn.data
        brukernavn = form.brukernavn.data
        passord = form.passord.data
        
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO kunder (navn, brukernavn, passord) VALUES (%s, %s, %s)",
            (navn, brukernavn, passord)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect("/login")

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    return render_template("register.html", form=form)

