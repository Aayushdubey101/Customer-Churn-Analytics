.PHONY: sync kernel test lint format verify

sync:
	uv sync

kernel:
	uv run python -m ipykernel install --user --name=customer-churn-analytics --display-name "Python (customer-churn-analytics)"

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run black .

verify:
	uv run python -c "import pandas, numpy, matplotlib, plotly, sklearn, sqlalchemy, dotenv, pytest, ruff; print('imports ok')"
