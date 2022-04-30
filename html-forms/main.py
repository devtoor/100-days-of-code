from __future__ import annotations

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    return f"<h1>Name: {request.form['username']}, Password: {request.form['password']}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
