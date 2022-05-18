from ensurepip import bootstrap
from flask import Flask

from flask_bootstrap import Bootstrap
from config import Config

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    Bootstrap(app)
    app.config.from_object('config.Config')

    with app.app_context():
        from .tls import tls
        from .bpki import bpki

        app.register_blueprint(tls.tls_bp)
        app.register_blueprint(bpki.bpki_bp)

        return app


