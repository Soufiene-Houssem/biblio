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
                        junit allowEmptyResults: true, testResults: 'app/analyse.xml'
                    }
                }
            }
        }
    }

}


