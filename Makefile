all: build run lint test docs coverage

build:
	@echo "Construction de l'image Docker..."
	docker-compose build

run:
	@echo "Exécution de l'application..."
	docker-compose up -d

lint:
	@echo "Exécution de pylint..."
	docker exec biblio-flask1 sh -c "find . -name '*.py' -exec pylint {} +" || true

test:
	@echo "Exécution de tests unitaires..."
	docker exec biblio-flask1 pytest || true

docs:
	@echo "Génération de documentation..."
	docker exec biblio-flask1 sh -c "pdoc -o docs run.py || true"

coverage:
	@echo "Analyser la couverture des tests..."
	docker exec biblio-flask1 coverage run -m pytest || true
	docker exec biblio-flask1 coverage report -m || true