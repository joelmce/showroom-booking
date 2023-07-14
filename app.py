from flask import Flask, render_template
from models.user import get_all
import os

app = Flask(__name__)

@app.route("/")
def index():
    results = get_all()
    return render_template("index.html", results=results)

app.run(debug=True)