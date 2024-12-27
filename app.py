from flask import Flask
from flask import render_template
from manager import blog_manager

app = Flask(__name__)

@app.route("/")
def home():
    posts = get_blog_posts()
    return render_template("index.html", posts = posts)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<post_id>")
def get_post(post_id):
    post = get_blog_post_by_id(post_id)
    print(post)
    return render_template("post.html", post = post)


def get_blog_posts():
    manager = blog_manager.BlogManager()
    return manager.get_blog_posts()


def get_blog_post_by_id(post_id):
    manager = blog_manager.BlogManager()
    return manager.get_blog_post_by_id(post_id)