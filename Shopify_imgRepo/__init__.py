from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # create and configure the app
    app = Flask(__name__)

    if app.config['ENV'] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config['ENV'] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    with app.app_context():

        from Shopify_imgRepo.auth import auth_bp
        app.register_blueprint(auth_bp)

        from Shopify_imgRepo.main import main_bp
        app.register_blueprint(main_bp)

        from Shopify_imgRepo.api import api_bp
        app.register_blueprint(api_bp)

        db.create_all()

    return app