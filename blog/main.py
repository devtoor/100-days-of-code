import requests as requests
from flask import Flask
from flask import render_template
from post import Post

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = [
    Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in posts
]


@app.route("/")
def home():
    return render_template("index.html", posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
