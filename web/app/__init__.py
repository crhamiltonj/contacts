from flask import Flask



def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .landing import routes

        app.register_blueprint(routes.landing_bp)
    

    return app
