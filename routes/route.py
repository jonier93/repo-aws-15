from flask import render_template, request, jsonify
from server import app
from database.db import *
from controllers.admin_s3 import *

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/consult_page')
def consult_page():
    return render_template("consult.html")

@app.route('/register_user', methods=["post"])
def register_user():
    data = request.form
    file = request.files
    id, name, lastname, birthday = data["id"], data["name"], data["lastname"], data["birthday"]
    photo = file["photo"]
    insert(id, name, lastname, birthday)
    session_s3 = connectionS3()
    photo_path, photo_name = save_file(id, photo)    
    upload_file_s3(session_s3, photo_path, photo_name)
    
    return "User added"

@app.route('/consult_user', methods=["post"])
def consult_user():
    id = request.get_json()
    result = consult(id)
    resp_data = {
        'name':result[0][1],
        'lastname':result[0][2],
        'birthday':result[0][3]
    }
    return jsonify(resp_data)

    