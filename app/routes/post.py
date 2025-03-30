from flask import Blueprint, request, url_for, render_template
from flask_login import login_required, current_user
from ..models import db, Post

post_bp = Blueprint("post", __name__)

@post_bp.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title').strip()
        content = request.form.get('content').strip()

        if not title or not content:
            content = f"Title ant content are required. <a href='{ url_for('post.new_post') }'>New post.</a>"
            return render_template("custom.html", title='Message', message=content)
        
        post = Post(title=title, content=content, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        
        content = f"Success. Post created! { post.id }"
        return render_template("custom.html", title='Message', message=content)
         
    return render_template("new-post.html")


