from flask import Flask, render_template, redirect
import mysql.connector
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "hemmelig-nok"  # samme som app.secret_key

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="fahad",
        password="Fahad2008",
        database="kantine"
    )

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO kunder (navn, brukernavn, passord, adresse) VALUES (%s, %s, %s, %s)",
            (form.name.data, form.username.data, form.password.data, form.adresse.data)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect("/login")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT navn FROM kunder WHERE brukernavn=%s AND passord=%s",
            (form.username.data, form.password.data)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            return render_template("welcome.html", name=user[0])
        form.username.errors.append("Feil brukernavn eller passord")

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)