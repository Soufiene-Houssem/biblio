all: run lint test docs coverage

run:
	@echo "Running the application..."
	docker-compose up -d

lint:
	@echo "Running pylint..."
	docker exec biblio-flask1 sh -c "find . -name '*.py' -exec pylint {} +" || true

test:
	@echo "Running unit tests..."
	docker exec biblio-flask1 pytest || true

docs:
	@echo "Generating documentation..."
	docker exec biblio-flask1 sh -c "pdoc -o docs run.py || true"

coverage:
	@echo "Checking code coverage..."
	docker exec biblio-flask1 coverage run -m pytest || true
	docker exec biblio-flask1 coverage report -m || true