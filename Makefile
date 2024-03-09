all: build run lint test docs coverage

build:
	@echo "Construction de l'image Docker..."
	docker-compose build

run:
	@echo "Exécution de l'application..."
	docker-compose up -d

lint:
	@echo "Exécution de pylint..."
	pylint --output-format=pylint_junit.JUnitReporter ./app/*.py > analyse.xml || true
