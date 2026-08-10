# Customer Churn Analytics

Enterprise-quality customer churn analytics project — Data Analyst portfolio piece.

## Stack

- Python 3.12+ / uv
- Jupyter, Pandas, NumPy, Scikit-learn
- SQLAlchemy + SQLite
- Plotly, Matplotlib
- Tableau Public
- pytest, Ruff, Black

## Structure

```
src/            application code
data/raw/       original, immutable source data
data/processed/ cleaned/transformed data
sql/            SQL scripts (schema, queries)
notebooks/      exploratory/analysis notebooks
reports/images/ exported chart images
reports/tableau/ Tableau workbooks/extracts
tests/          pytest test suite
scripts/        one-off/utility scripts
docs/           project documentation
```

## Setup

```
uv sync
cp .env.example .env
```

## Status

Project skeleton only — analytics not yet implemented.
