# Learning Platform Analytics

Analysis of student engagement, purchases, ratings, and assessments on a learning platform to identify key opportunities for improvement.

## Features

- Modular Python + SQL codebase
- Demonstrates: Summarizing Data, JOINs, Subqueries, Window Functions
- Uses modern tooling: uv, DVC, SQLite
- Clean, maintainable structure

## Project Structure

```markdown
learning-platform-analytics/
├── pyproject.toml
├── README.md
├── setup.sh
├── schema.sql
├── config.py
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── queries.py
│   ├── utils.py
│   └── analysis.py
├── notebook.ipynb
├── data/                    # Raw CSVs (managed by DVC)
├── learning_platform.db     # Generated SQLite database
├── .dvc/
└── .venv/

## Quick Start
### Using Setup Script (Recommended)

# 1. Make script executable
chmod +x setup.sh

# 2. Run setup
./setup.sh

uv run dvc pull          # Download raw data
uv run jupyter lab       # Start Jupyter Lab

## Manual Setup
uv sync --extra dev
uv run dvc init --no-scm
uv run dvc add data                  # First time only
uv run python -m ipykernel install --user --name=learning-platform --display-name="Python (Learning Platform)"
uv run jupyter lab

## Commands Cheat Sheet

Command,Description
./setup.sh,Run full project setup
uv sync --extra dev,Install/update dependencies
uv run dvc pull,Download raw CSV data
uv run dvc push,Upload data to remote
uv run jupyter lab,Start Jupyter Lab
uv run dvc status,Check data status

## Development
# Format code
uv run black .
uv run isort .

# Run setup again after changes
./setup.sh