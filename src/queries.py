# src/queries.py
import pandas as pd

def get_kpi_summary(conn):
    """Overall platform KPIs."""
    query = """
    SELECT 
        COUNT(DISTINCT si.student_id) AS total_students,
        COUNT(DISTINCT ci.course_id) AS total_courses,
        COUNT(DISTINCT sp.purchase_id) AS total_purchases,
        ROUND(SUM(sp.amount_paid), 2) AS total_revenue,
        ROUND(AVG(cr.rating), 2) AS avg_rating,
        ROUND(AVG(se.engagement_score), 2) AS avg_engagement_score,
        ROUND(AVG(sl.progress_percent), 2) AS avg_progress
    FROM student_info si
    CROSS JOIN course_info ci
    LEFT JOIN student_purchases sp ON 1=1
    LEFT JOIN course_ratings cr ON 1=1
    LEFT JOIN student_engagement se ON 1=1
    LEFT JOIN student_learning sl ON 1=1
    LIMIT 1;
    """
    return pd.read_sql(query, conn)

def get_category_performance(conn):
    """Performance metrics by course category."""
    query = """
    SELECT 
        ci.category,
        COUNT(DISTINCT sp.student_id) AS unique_buyers,
        COUNT(DISTINCT se.student_id) AS engaged_students,
        ROUND(AVG(cr.rating), 2) AS avg_rating,
        ROUND(AVG(se.engagement_score), 2) AS avg_engagement_score,
        ROUND(AVG(sl.progress_percent), 2) AS avg_progress,
        ROUND(SUM(sp.amount_paid), 2) AS category_revenue
    FROM course_info ci
    LEFT JOIN student_purchases sp ON ci.course_id = sp.course_id
    LEFT JOIN student_engagement se ON ci.course_id = se.course_id
    LEFT JOIN course_ratings cr ON ci.course_id = cr.course_id
    LEFT JOIN student_learning sl ON ci.course_id = sl.course_id
    GROUP BY ci.category
    ORDER BY avg_engagement_score ASC;
    """
    return pd.read_sql(query, conn)

def get_student_journey(conn):
    """Student journey analysis per course."""
    query = """
    SELECT 
        ci.course_name,
        ci.category,
        ci.price,
        COUNT(DISTINCT sp.student_id) AS total_buyers,
        COUNT(DISTINCT sl.student_id) AS learners,
        COUNT(DISTINCT se.student_id) AS actively_engaged,
        ROUND(100.0 * COUNT(DISTINCT se.student_id) / 
             NULLIF(COUNT(DISTINCT sp.student_id), 0), 2) AS engagement_rate_pct,
        ROUND(AVG(cr.rating), 2) AS avg_rating,
        ROUND(AVG(sl.progress_percent), 2) AS avg_progress
    FROM course_info ci
    LEFT JOIN student_purchases sp ON ci.course_id = sp.course_id
    LEFT JOIN student_learning sl ON ci.course_id = sl.course_id
    LEFT JOIN student_engagement se ON ci.course_id = se.course_id
    LEFT JOIN course_ratings cr ON ci.course_id = cr.course_id
    GROUP BY ci.course_name, ci.category, ci.price
    HAVING total_buyers >= 10
    ORDER BY engagement_rate_pct ASC;
    """
    return pd.read_sql(query, conn)

def get_underperforming_courses(conn):
    """Courses performing below category average."""
    query = """
    SELECT 
        ci.course_name,
        ci.category,
        ROUND(AVG(se.engagement_score), 2) AS course_engagement,
        (SELECT ROUND(AVG(se2.engagement_score), 2)
         FROM student_engagement se2
         JOIN course_info ci2 ON se2.course_id = ci2.course_id
         WHERE ci2.category = ci.category) AS category_avg_engagement,
        ROUND(AVG(sl.progress_percent), 2) AS avg_progress
    FROM course_info ci
    JOIN student_engagement se ON ci.course_id = se.course_id
    JOIN student_learning sl ON ci.course_id = sl.course_id
    GROUP BY ci.course_name, ci.category
    HAVING course_engagement < category_avg_engagement * 0.85;
    """
    return pd.read_sql(query, conn)

def get_engagement_ranking(conn):
    """Ranking of courses by engagement within category."""
    query = """
    WITH course_metrics AS (
        SELECT 
            ci.course_name,
            ci.category,
            ROUND(AVG(se.engagement_score), 2) AS avg_engagement,
            ROUND(AVG(sl.progress_percent), 2) AS avg_progress,
            COUNT(DISTINCT sp.student_id) AS buyers
        FROM course_info ci
        LEFT JOIN student_engagement se ON ci.course_id = se.course_id
        LEFT JOIN student_learning sl ON ci.course_id = sl.course_id
        LEFT JOIN student_purchases sp ON ci.course_id = sp.course_id
        GROUP BY ci.course_name, ci.category
    )
    SELECT *,
           RANK() OVER (PARTITION BY category ORDER BY avg_engagement DESC) AS rank_in_category
    FROM course_metrics
    ORDER BY category, rank_in_category;
    """
    return pd.read_sql(query, conn)

def get_mom_trend(conn):
    """Month-over-month engagement trend."""
    query = """
    SELECT 
        strftime('%Y-%m', session_date) AS month,
        ROUND(AVG(engagement_score), 2) AS monthly_eng_score,
        LAG(ROUND(AVG(engagement_score), 2)) OVER (ORDER BY strftime('%Y-%m', session_date)) AS prev_month_score,
        ROUND(100.0 * (AVG(engagement_score) - 
             LAG(AVG(engagement_score)) OVER (ORDER BY strftime('%Y-%m', session_date))) 
             / LAG(AVG(engagement_score)) OVER (ORDER BY strftime('%Y-%m', session_date)), 2) AS mom_change_pct
    FROM student_engagement
    GROUP BY month
    ORDER BY month;
    """
    return pd.read_sql(query, conn)