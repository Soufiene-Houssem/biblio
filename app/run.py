"""
Fichier principal de l'application Flask.
"""

from flask import Flask
from models.model import db
from configs.config import Config, cache
from routes import app_routes


app = Flask(__name__)

cache.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

app.register_blueprint(app_routes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
