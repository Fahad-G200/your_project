from flask import Flask, render_template, request, redirect
import mysql.connector
from forms import RegisterForm, Loginform

app = Flask(__name__)
app.secret_key = "hemmelig-nok"
