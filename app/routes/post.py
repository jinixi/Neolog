from flask import Blueprint, request, url_for, render_template, redirect
from flask_login import login_required, current_user
from ..models import db, Post, User

post_bp = Blueprint("post", __name__)

@post_bp.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title').strip()
        content = request.form.get('content').strip()

        if not title or not content:
            return render_template("error.html")
        
        post = Post(title=title, content=content, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        
        return redirect(url_for('index.index'))
         
    return render_template("new-post.html")


@post_bp.route("/post/<int:id>")
def post_page(id):
    post = Post.query.get(id)
    if not post:
        return render_template("error.html")
    
    author = User.query.get(post.user_id)
    return render_template("post.html", post=post, author=author)