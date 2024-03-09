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
                    archiveArtifacts artifacts: 'lint_report.xml', fingerprint: true
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
                    archiveArtifacts artifacts: 'test_report.xml', fingerprint: true
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
                    archiveArtifacts artifacts: 'docs/*.html', fingerprint: true
                }
            }
        }
        stage('Couverture des tests') {
            steps {
                echo 'Analyse de la couverture des tests...'
                sh 'make coverage'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'coverage_report.xml', fingerprint: true
                }
            }
        }
    }
}
