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
        junit 'reports/LINT-lints*.xml'
      }
    }

    stage('Tests unitaires') {
      steps {
        echo 'Exécution des tests unitaires...'
        sh 'make test'
        junit 'reports/TEST-tests*.xml'
      }
    }

    stage('Génération de documentation') {
      steps {
        echo 'Generation de la documentation...'
        sh 'make docs'
        junit 'reports/DOCS-docs*.xml'
      }
    }

  }
}
