from flask import Flask, render_template, request, redirect
import mysql.connector
from forms import RegisterForm, Loginform

app = Flask(__name__)
app.secret_key = "hemmelig-nok"


def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="DIN_DB_BRUKER",
        password="DITT_PASSORD",
        database="DIN_DATABASE" 
    )