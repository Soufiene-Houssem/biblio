all: build lint test docs coverage

build:
	@echo "Construction de l'image Docker..."
	docker-compose run -d --build

lint: prepare
	@echo "Exécution de pylint..."
	docker exec biblio-flask1 sh -c "pylint --disable=missing-docstring,trailing-whitespace --output-format=pylint_junit.JUnitReporter ./*.py --output=TEST-pylint_report.xml" || true

test: prepare
	@echo "Exécution des tests unitaires..."
	docker exec biblio-flask1 pytest --junitxml=TEST-test_results.xml || true

docs: prepare
	@echo "Génération de la documentation..."
	docker exec biblio-flask1 sh -c "pdoc -o reports/docs run.py || true"

coverage: prepare
	@echo "Analyser la couverture des tests..."
	docker exec biblio-flask1 coverage run -m pytest || true
	docker exec biblio-flask1 coverage report -m || true
	docker exec biblio-flask1 coverage xml -o reports/coverage_report.xml || true

prepare:
	@mkdir -p app/reports