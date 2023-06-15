from flask import Flask
from flask_migrate import Migrate
from drRichie.extras.extensions import db, login_manager



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12309845876'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    """extension initialization"""
    app.app_context().push()
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from drRichie.extras.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

   
    """--------------------Blueprint Registration---------------------"""
    from .authentication.views import auth
    app.register_blueprint(auth)
    from drRichie.dashboard.views import dash
    app.register_blueprint(dash)

    return app


    