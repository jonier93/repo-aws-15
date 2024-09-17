from flask import render_template, request
from server import app
from database.db import *

@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/consult_page')
def consult_page():
    return render_template("consult.html")

@app.route('/register_user', methods=["post"])
def register_user():
    data = request.form
    id, name, lastname, birthday = data["id"], data["name"], data["lastname"], data["birthday"]
    insert(id, name, lastname, birthday)
    return "User added"

@app.route('/consult_user', methods=["post"])
def consult_user():
    id = request.get_json()
    result = consult(id)
    print(result)
    return "El usuario ha sido consultado"

    