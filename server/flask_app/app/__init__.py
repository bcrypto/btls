from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config=False)
Bootstrap(app)
app.config.from_object('config.Config')

with app.app_context():
    from .tls import tls
    app.register_blueprint(tls.tls_bp)


