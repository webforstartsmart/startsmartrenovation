from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_session import Session
from werkzeug.utils import secure_filename

#configure application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


app.run(debug=True)