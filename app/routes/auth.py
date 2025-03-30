from flask import Blueprint, redirect, url_for, request, render_template
from flask_login import login_user, logout_user, login_required, current_user
from ..models import User, db 
from ..utils import validate_username, validate_password


auth_bp = Blueprint("auth", __name__, url_prefix='/auth')


@auth_bp.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        redirect(url_for("index.index"))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        username = username.strip().lower()

        if not username or not password:
            return render_template("error.html")
        
        if User.query.filter_by(username=username).first():
            return render_template("error.html")
        
        if validate_username(username) or validate_password(password):
            return render_template("error.html")

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter_by(username=username).first()
        login_user(user, remember=True)

        return redirect(url_for('index.index'))

    return render_template('sign-up.html')


@auth_bp.route("/sign-in", methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        redirect(url_for("index.index"))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        username = username.strip().lower()

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user, remember=True)
            return redirect(url_for("index.index"))
        return render_template("error.html")

    return render_template("sign-in.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.index"))
