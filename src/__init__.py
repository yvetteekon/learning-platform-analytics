# src/__init__.py
from .database import get_connection, create_schema, load_all_data
from .queries import (
    get_kpi_summary,
    get_category_performance,
    get_student_journey,
    get_underperforming_courses,
    get_engagement_ranking,
    get_mom_trend,
)
from .utils import plot_category_performance, plot_engagement_trend

__all__ = [
    "get_connection",
    "create_schema",
    "load_all_data",
    "get_kpi_summary",
    "get_category_performance",
    "get_student_journey",
    "get_underperforming_courses",
    "get_engagement_ranking",
    "get_mom_trend",
    "plot_category_performance",
    "plot_engagement_trend",
]