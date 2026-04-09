# src/utils.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_category_performance(df):
    """Plot average rating vs engagement by category."""
    df.plot(x="category", y=["avg_rating", "avg_engagement_score"], kind="bar")
    plt.title("Average Rating vs Engagement Score by Category")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_engagement_trend(df):
    """Plot month-over-month engagement trend."""
    df.plot(x="month", y="monthly_eng_score", marker="o")
    plt.title("Monthly Engagement Score Trend")
    plt.ylabel("Average Engagement Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()