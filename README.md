# Learning Platform Analytics

**Identifying Growth Opportunities**

This project analyzes student behavior on a learning platform (purchases, engagement, learning progress, ratings, quizzes, exams, and community questions) to uncover actionable insights for improvement.

## 📊 What the Notebook Covers

- **Phase 1**: Database setup and data loading from CSVs
- **Phase 2**: Summarizing data with SQL (KPIs by category)
- **Phase 3**: Combining tables using JOINs (student journey analysis)
- **Phase 4**: Subqueries (benchmarking courses against category averages)
- **Phase 5**: Window functions (ranking, percentiles, month-over-month trends)
- **Phase 6**: Key opportunities & business recommendations

## 🛢️ Data Source
- 365 Learning Data Challenge (October 2022) 

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
```

## 🔄 Reproducibility

- All dependencies are managed via `uv` and `pyproject.toml`
- Raw data is versioned with DVC
- Run `uv run dvc pull` to ensure you have the latest dataset
- The entire analysis can be reproduced from scratch

## 🚀 Quick Start
### Option 1: Using the Setup Script (Recommended)

The easiest way to set up the project is by using the included `setup.sh` script:

```bash
# 1. Make the script executable
chmod +x setup.sh

# 2. Run the setup
./setup.sh
```
After the script finishes, run:

```bash
uv run dvc pull          # Download the raw CSV data
uv run jupyter lab       # Start Jupyter Lab
```

**Important**: In Jupyter Lab, select the kernel "Python (Learning Platform)" from the top right

### Option 2: Manual Setup

### 1. Clone the repository
```bash
git clone https://github.com/yvetteekon/learning-platform-analytics.git
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

**Important**: In Jupyter Lab, select the kernel "Python (Learning Platform)" from the top right


## 📌 Commands Cheat Sheet

| Command                                    | Description                                      |
|--------------------------------------------|--------------------------------------------------|
| `./setup.sh`                               | Run full project setup (recommended)             |
| `uv sync --extra dev`                      | Install/update all dependencies (including DVC)  |
| `uv run dvc init`                          | Initialize DVC in the project                    |
| `uv run dvc add data`                      | Track the `data/` folder with DVC                |
| `uv run dvc pull`                          | Download data from Google Drive                  |
| `uv run dvc push`                          | Upload data to Google Drive                      |
| `uv run python -m ipykernel install --user --name=learning-platform --display-name="Python (Learning Platform)"` | Register Jupyter kernel |
| `uv run jupyter lab`                       | Start Jupyter Lab                                |
| `uv run dvc status`                        | Check data status                                |

