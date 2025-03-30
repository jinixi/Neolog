from flask import Flask
from .extensions import db, login_manager
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #reqister blueprints 
    from .routes.index import index_bp
    app.register_blueprint(index_bp)

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from .routes.post import post_bp
    app.register_blueprint(post_bp)
    
    #login manager init
    login_manager.init_app(app)
    login_manager.login_view = 'auth.sign_in'

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    #init db 
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
