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
            post {
                always {
                    script {
                        junit allowEmptyResults: true, testResults: 'lint_report.xml'
                    }
                }
            }
        }
        stage('Tests unitaires') {
            steps {
                echo 'Exécution des tests unitaires...'
                sh 'make test'
            }
            post {
                always {
                    script {
                        junit allowEmptyResults: true, testResults: 'test_report.xml'
                    }
                }
            }
        }
        stage('Génération de documentation') {
            steps {
                echo 'Génération de la documentation...'
                sh 'make docs'
            }
            post {
                always {
                    script {
                        junit allowEmptyResults: true, testResults: 'docs_report.xml'
                    }
                }
            }
        }
    }
}
