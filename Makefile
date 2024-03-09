all: build run lint test docs coverage

build:
	@echo "Construction de l'image Docker..."
	docker-compose build

run:
	@echo "Exécution de l'application..."
	docker-compose up -d

lint:
	@echo "Exécution de pylint..."
	docker exec biblio-flask1 sh -c "pylint --output-format=pylint_junit.JUnitReporter ./run.py > lint_report.xml" || true
