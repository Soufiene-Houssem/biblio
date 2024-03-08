from flask import render_template, Blueprint, jsonify
from datetime import datetime
from models.model import Livre
from models.model  import Editeur
from models.model  import Categorie
from sqlalchemy.orm import joinedload

import pytz
from configs.config import cache

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    montreal_tz = pytz.timezone('America/Toronto')
    montreal_time = datetime.now(montreal_tz).strftime('%Y-%m-%d %H:%M:%S')
    message = "Biblio"
    return render_template('index.html', date=montreal_time, message=message)

@app_routes.route('/livres')
@cache.cached(timeout=10)
def get_livres():
    livres = cache.get('livres')
    categories = Categorie.query.all()
    if livres is None:
        livres = Livre.query.options(
            joinedload(Livre.editeur),
            joinedload(Livre.categories),
            joinedload(Livre.auteurs) 
        ).all()
        cache.set('livres', livres, timeout=50)
        
    return render_template('livres.html', books=livres, categories=categories)

@app_routes.route('/contenu-cache')
def cache_content():
    cached_livres = cache.get('livres') 
    if cached_livres:
        return render_template('cache.html', cached_books=cached_livres)
    else:
        message = 'Aucun contenu dans le cache'
        return render_template('cache.html', message=message)

