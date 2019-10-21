from flask import Flask
from .db import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .landing import landing_routes
        from .contacts import contacts_routes

        app.register_blueprint(landing_routes.landing_bp)
        app.register_blueprint(contacts_routes.contact_bp, url_prefix="/contacts")
    
        create_tables()

    return app


def create_tables():
    from .models import Contact
    db.create_all()

