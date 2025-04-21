from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Inicjalizacja db i migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicjalizacja db i migrate z aplikacją
    db.init_app(app)
    migrate.init_app(app, db)

    # Importowanie modeli wewnątrz funkcji create_app
    from blog import models

    # Rejestracja blueprinta
    from blog.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
