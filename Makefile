check:
	poetry run ruff check xlsx_data_stream/ scripts/ tests/
	poetry run ruff format --check xlsx_data_stream/ scripts/ tests/
	poetry run pyright xlsx_data_stream/ scripts/ tests/

test:
	poetry run pytest tests/

fix:
	poetry run ruff check --fix xlsx_data_stream/ scripts/ tests/
	poetry run ruff format xlsx_data_stream/ scripts/ tests/

sample:
	poetry run python scripts/generate_sample.py
