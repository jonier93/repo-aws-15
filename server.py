from flask import Flask, render_template
from database.db import *

app = Flask(__name__)

@app.route('/register_page')
def register_page():
    return render_template("register.html")

@app.route('/register_user')
def register_user():
    insert()
    return "User added"
     
if __name__ == "__main__":    
    host = "127.0.0.1"
    port = 8000
    app.run(host, port, True)

    