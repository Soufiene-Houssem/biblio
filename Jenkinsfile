pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Construction de l\'image Docker...'
                sh 'make build'
            }
        }
        stage('Analyse statique') {
            steps {
                echo 'Analyse statique du code en cours...'
                sh 'make lint'
            }
        }
        stage('Tests unitaires') {
            steps {
                echo 'Exécution des tests unitaires...'
                sh 'make test'
            }
        }
        stage('Génération de documentation') {
            steps {
                echo 'Génération de la documentation...'
                sh 'make docs'
            }
        }
        stage('Couverture de code') {
            steps {
                echo 'Analyse de la couverture de code...'
                sh 'make coverage'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'lint_report.xml, test_report.xml, docs_report.xml, coverage_report.xml', allowEmptyArchive: true
            junit '**/test_report.xml'
        }
    }

}


