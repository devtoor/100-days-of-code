import os
import smtplib

import requests
from dotenv import load_dotenv
from flask import Flask
from flask import render_template
from flask import request

posts = requests.get(
    "https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw"
    "/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json",
).json()

load_dotenv()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form = request.form
        send_email(form["name"], form["email"], form["phone"], form["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(os.getenv("EMAIL_SMTP"), port=587) as connection:
        connection.starttls()
        connection.login(os.getenv("EMAIL"), os.getenv("EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("EMAIL"),
            to_addrs=os.getenv("EMAIL"),
            msg=email_message,
        )


if __name__ == "__main__":
    app.run(debug=True)
