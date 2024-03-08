pipeline {
    agent any

    stages {
        stage('Analyse statique') {
            steps {
                echo '~~~~~~~~Analyse statique du code en cours...'
                sh -c 'find . -name \'*.py\' -exec pylint {} +'
            }
        }
        stage('Tests unitaires') {
            steps {
                echo '~~~~~~~~Exécution des tests unitaires...'
                sh 'pytest'
            }
        }
        stage('Génération de documentation') {
            steps {
                echo '~~~~~~~~Génération de la documentation...'
                sh -c 'pdoc -o docs run.py'
            }
        }
        stage('Couverture du code') {
            steps {
                echo '~~~~~~~~Calcul de la couverture du code...'
                sh 'coverage run -m pytest'
                sh 'coverage report -m'
            }
        }
    }
}
