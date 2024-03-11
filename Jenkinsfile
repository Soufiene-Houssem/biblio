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
                junit 'reports/TEST-tests*.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'reports/lint_report.xml'
                }
            }
        }
        stage('Tests unitaires') {
            steps {
                echo 'Exécution des tests unitaires...'
                sh 'make test'
                junit 'reports/TEST-tests*.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'reports/test_report.xml'
                }
            }
        }
        stage('Génération de documentation') {
            steps {
                echo 'Génération de la documentation...'
                sh 'make docs'
                junit 'reports/TEST-tests*.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'reports/docs_report.xml'
                }
            }
        }
        stage('Couverture de code') {
            steps {
                echo 'Analyse de la couverture de code...'
                sh 'make coverage'
                junit 'reports/TEST-tests*.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'reports/coverage_report.xml'
                }
            }
        }
    }
}
