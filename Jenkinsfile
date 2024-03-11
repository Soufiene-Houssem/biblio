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
					junit allowEmptyResults: true, testResults: 'app/analyse.xml'
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
					junit 'TEST-test_results.xml'
				}
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
}
