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
        junit 'reports/test_report.xml'
      }
    }

    stage('Génération de documentation') {
      steps {
        echo 'Generation de la documentation...'
        sh 'make docs'
      }
    }

  }
}
