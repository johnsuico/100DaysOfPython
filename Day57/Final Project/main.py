from flask import Flask, render_template
from post import Post
import requests as req

res = req.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
posts = []
for post in res:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    posts.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<blog_id>')
def get_post(blog_id):
    return render_template('post.html', post=posts[int(blog_id)-1])

if __name__ == "__main__":
    app.run(debug=True)
