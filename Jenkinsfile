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
      post {
        always {
          script {
            junit allowEmptyResults: true, testResults: 'lint_report.xml'
          }

        }

      }
      steps {
        echo 'Analyse statique du code en cours...'
        sh 'make lint'
      }
    }

    stage('Tests unitaires') {
      post {
        always {
          script {
            junit allowEmptyResults: true, testResults: 'test_report.xml'
          }

        }

      }
      steps {
        echo 'Exécution des tests unitaires...'
        sh 'make test'
      }
    }

    stage('Génération de documentation') {
      post {
        always {
          script {
            junit allowEmptyResults: true, testResults: 'docs_report.xml'
          }

        }

      }
      steps {
        echo 'Generation de la documentation...'
        sh 'make docs'
      }
    }

  }
}