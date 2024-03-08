CREATE DATABASE IF NOT EXISTS biblio;
USE biblio;

CREATE TABLE auteur (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

CREATE TABLE categorie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(10) NOT NULL,
    nom VARCHAR(100) NOT NULL
);

CREATE TABLE editeur (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

CREATE TABLE livre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    description TEXT,
    isbn VARCHAR(20),
    annee_apparition INT,
    image VARCHAR(100),
    editeur_id INT,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (editeur_id) REFERENCES editeur(id)
);

CREATE TABLE livre_auteur (
    livre_id INT,
    auteur_id INT,
    FOREIGN KEY (livre_id) REFERENCES livre(id),
    FOREIGN KEY (auteur_id) REFERENCES auteur(id),
    PRIMARY KEY (livre_id, auteur_id)
);

CREATE TABLE livre_categorie (
    livre_id INT,
    categorie_id INT,
    FOREIGN KEY (livre_id) REFERENCES livre(id),
    FOREIGN KEY (categorie_id) REFERENCES categorie(id),
    PRIMARY KEY (livre_id, categorie_id)
);
