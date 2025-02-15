.PHONY: setup clean test lint format

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install poetry
	. .venv/bin/activate && poetry install

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test:
	. .venv/bin/activate && pytest

lint:
	. .venv/bin/activate && flake8 .
	. .venv/bin/activate && black . --check
	. .venv/bin/activate && isort . --check-only

format:
	. .venv/bin/activate && black .
	. .venv/bin/activate && isort . 