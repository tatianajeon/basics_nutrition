from flask import Flask
from .site.routes import site
from .api.routes import api
from .authentication.routes import auth
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db as root_db, login_manager, ma
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from basics_app.helpers import JSONEncoder
import os

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0', port=port, debug=True)

app.register_blueprint(site)
app.register_blueprint(api)
app.register_blueprint(auth)

app.config.from_object(Config)

root_db.init_app(app)

migrate= Migrate(app, root_db)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

app.json_encoder = JSONEncoder

CORS(app)