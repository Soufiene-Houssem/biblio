from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Auteur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    livres = db.relationship('Livre', secondary='livre_auteur', back_populates='auteurs')

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False) 
    nom = db.Column(db.String(100), nullable=False)
    livres = db.relationship('Livre', secondary='livre_categorie', back_populates='categories')

class Editeur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)

class Livre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    isbn = db.Column(db.String(20), nullable=False)
    annee_apparition = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    editeur_id = db.Column(db.Integer, db.ForeignKey('editeur.id'), nullable=False)
    date_creation = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)  # Ajout de la colonne date_creation
    date_modification = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)  # Ajout de la colonne date_modification
    editeur = db.relationship('Editeur', backref=db.backref('livres', lazy=True))
    auteurs = db.relationship('Auteur', secondary='livre_auteur', back_populates='livres')
    categories = db.relationship('Categorie', secondary='livre_categorie', back_populates='livres')

class LivreAuteur(db.Model):
    __tablename__ = 'livre_auteur'
    livre_id = db.Column(db.Integer, db.ForeignKey('livre.id'), primary_key=True)
    auteur_id = db.Column(db.Integer, db.ForeignKey('auteur.id'), primary_key=True)

class LivreCategorie(db.Model):
    __tablename__ = 'livre_categorie'
    livre_id = db.Column(db.Integer, db.ForeignKey('livre.id'), primary_key=True)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), primary_key=True)
