from flask import Blueprint, render_template
from ..models import Post, User

index_bp = Blueprint("index", __name__)

@index_bp.route("/")
@index_bp.route("/page/<int:page>")
def index(page=1):
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=5, error_out=False)
    return render_template("index.html", posts=posts, user=User)
