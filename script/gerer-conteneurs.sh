#!/bin/bash

creer_environnement() {
    echo "Création de l'environnement de développement..."
    docker-compose up --build
}

creer_db() {
    echo "Création de la base de données..."
    source .env
    docker exec -i biblio-mysql mysql -uroot -p"${MYSQL_ROOT_PASSWORD}" biblio < ./db/db.sql
}

importer_livres() {
    echo "Importation  des livres dans la base de données..."
    source .env
    python3 ./script/inserer_livres.py
    docker exec -i biblio-mysql mysql -uroot -p"${MYSQL_ROOT_PASSWORD}" biblio < ./data/livres_insertion.sql
}

supprimer_environnement() {
    echo "Suppression de l'environnement de développement..."
    docker-compose down --volumes
    docker-compose down --rmi all
    docker-compose down --remove-orphans
    docker-compose down
}

demarrer_conteneurs() {
    echo "Démarrage des conteneurs..."
    docker-compose start
}

arreter_conteneurs() {
    echo "Arrêt des conteneurs..."
    docker-compose stop
}

menu_principal() {
    echo "Menu Principal"
    echo "1. Créer l'environnement de développement"
    echo "2. Créer la base de données"
    echo "3. Importer des livres"
    echo "4. Supprimer l'environnement de développement"
    echo "5. Démarrer les conteneurs"
    echo "6. Arrêter les conteneurs"
    echo "7. Quitter"
    read -p "Choisissez une option : " choix
    echo
    case $choix in
        1) creer_environnement ;;
        2) creer_db ;;
        3) importer_livres ;;
        4) supprimer_environnement ;;
        5) demarrer_conteneurs ;;
        6) arreter_conteneurs ;;
        7) exit ;;
        *) echo "Option invalide"; menu_principal ;;
    esac
}

if [ $# -eq 0 ]; then
    menu_principal
else
    case "$1" in
        "creer")
            creer_environnement
            ;;
        "creer_db")
            creer_db
            ;;
        "importer")
            importer_livres
            ;;
        "supprimer")
            supprimer_environnement
            ;;
        "demarrer")
            demarrer_conteneurs
            ;;
        "arreter")
            arreter_conteneurs
            ;;
        *)
            echo "Utilisation: $0 [creer|creer_db|importer|supprimer|demarrer|arreter]"
            exit 1
            ;;
    esac
fi
