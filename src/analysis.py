# src/analysis.py
import pandas as pd

def identify_key_opportunities(conn):
    """Identify high-priority business opportunities."""
    query = """
    SELECT 
        ci.course_name,
        ci.category,
        COUNT(DISTINCT sp.student_id) AS total_buyers,
        ROUND(AVG(se.engagement_score), 2) AS avg_engagement,
        ROUND(AVG(sl.progress_percent), 2) AS avg_progress,
        ROUND(AVG(cr.rating), 2) AS avg_rating
    FROM course_info ci
    LEFT JOIN student_purchases sp ON ci.course_id = sp.course_id
    LEFT JOIN student_engagement se ON ci.course_id = se.course_id
    LEFT JOIN student_learning sl ON ci.course_id = sl.course_id
    LEFT JOIN course_ratings cr ON ci.course_id = cr.course_id
    GROUP BY ci.course_name, ci.category
    HAVING total_buyers >= 20 
       AND avg_engagement < 60
    ORDER BY avg_engagement ASC;
    """
    return pd.read_sql(query, conn)


def get_quiz_performance_issues(conn):
    """Identify courses with low quiz scores that may impact engagement."""
    query = """
    SELECT 
        ci.course_name,
        ROUND(AVG(sq.score), 2) AS avg_quiz_score,
        ROUND(AVG(se.engagement_score), 2) AS avg_engagement,
        COUNT(DISTINCT sq.student_id) AS quiz_attempts
    FROM course_info ci
    JOIN student_quizzes sq ON ci.course_id = sq.course_id
    JOIN student_engagement se ON ci.course_id = se.course_id
    GROUP BY ci.course_name
    HAVING avg_quiz_score < 65
    ORDER BY avg_quiz_score ASC;
    """
    return pd.read_sql(query, conn)