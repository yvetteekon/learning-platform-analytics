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
learning-platform-analytics/
├── pyproject.toml
├── README.md
├── .gitignore
├── data/                  # Raw CSVs (tracked by DVC, ignored by Git)
├── notebook.ipynb         # Main analysis notebook
├── learning_platform.db   # Generated SQLite database
├── .dvc/                  # DVC configuration
├── data.dvc               # DVC pointer file for the data folder
└── .venv/                 # Virtual environment (created by uv)


## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd learning-platform-analytics

### 2. Set up the environment with uv
Bash# Install dependencies (including DVC)
uv sync --extra dev
3. Pull the data using DVC
Bash# Download the actual CSV files (they are not stored in Git)
uv run dvc pull
4. Start Jupyter Notebook
Bash# Register the kernel (first time only)
uv run ipykernel install --user --name=learning-platform --display-name="Python (Learning Platform)"

# Launch Jupyter Lab
uv run jupyter lab