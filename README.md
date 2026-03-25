# Learning Platform Analytics

**Identifying Growth Opportunities using SQLite + DVC**

This project analyzes student behavior on a learning platform (purchases, engagement, learning progress, ratings, quizzes, exams, and community questions) to uncover actionable insights for improvement.

## 🎯 Objectives
- Demonstrate core SQL skills: summarization, JOINs, subqueries, and window functions
- Build a reproducible analytics workflow using modern tools
- Identify high-impact opportunities such as content refresh, retention campaigns, and assessment improvements

## 🛠️ Tech Stack
- **Python** 3.11+
- **SQLite** – Database
- **uv** – Lightning-fast package manager & virtual environment
- **DVC** – Data Version Control (manages raw CSVs outside Git)
- **Jupyter Notebook** + **pandas**, **matplotlib**, **seaborn**
- **Black**, **isort**, **flake8** – Code quality

## 📁 Project Structure
```bash
learning-platform-analytics/
├──pyproject.toml                 # Project configuration & dependencies (uv)
├──README.md                      # This file
├──.gitignore                     # Git ignore rules (includes DVC + data)
├──data/                          # Raw CSV files (versioned with DVC)
├──notebook.ipynb                 # Main Jupyter Notebook with all SQL analysis
├──learning_platform.db           # SQLite database (generated)
├──.dvc/                          # DVC internal configuration
├──data.dvc                       # DVC pointer file (committed to Git)
└──.venv/                         # Virtual environment managed by uv


## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd learning-platform-analytics
```

### 2. Set up the environment with uv
```bash
# Install dependencies (including DVC)
uv sync --extra dev
```

### 3. Pull the data using DVC
```bash
# Download the actual CSV files (they are not stored in Git)
uv run dvc pull
```

### 4. Start Jupyter Notebook
```bash
# Register the kernel (first time only)
uv run ipykernel install --user --name=learning-platform --display-name="Python (Learning Platform)"

# Launch Jupyter Lab
uv run jupyter lab
```

```markdown
> **Important**: In Jupyter Lab, select the kernel "Python (Learning Platform)" from the top right
```

## 📊 What the Notebook Covers

**Phase 1**: Database setup and data loading from CSVs
**Phase 2**: Summarizing data with SQL (KPIs by category)
**Phase 3**: Combining tables using JOINs (student journey analysis)
**Phase 4**: Subqueries (benchmarking courses against category averages)
**Phase 5**: Window functions (ranking, percentiles, month-over-month trends)
**Phase 6**: Key opportunities & business recommendations

## 🔄 Reproducibility

All dependencies are managed via uv and pyproject.toml
Raw data is versioned with DVC
Run uv run dvc pull to ensure you have the latest dataset
The entire analysis can be reproduced from scratch

## 🧩 How to Contribute / Extend

Add new CSVs → uv run dvc add data/new_file.csv
Update analysis → edit notebook.ipynb
Format code before committing:Bashuv run black .
uv run isort .

## 📌 Commands Cheat Sheet

































CommandDescriptionuv sync --extra devInstall/update all dependenciesuv run dvc pullDownload latest datauv run dvc pushUpload data to remote storageuv run jupyter labStart Jupyter Labuv run dvc statusCheck data statusuv run black .Format code

Made with ❤️ using modern data tools
Feel free to reach out if you have any questions or suggestions!