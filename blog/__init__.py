from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os

# Inicjalizacja db i migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = os.urandom(24)  # Ustawienie klucza tajnego

    db.init_app(app)
    migrate.init_app(app, db)

    from blog import models
    from blog.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app