#!/bin/bash
# run_tests.sh - Automated test script for Learning Platform Analytics

echo "================================================================"
echo "   Learning Platform Analytics - Automated Tests"
echo "================================================================"

# Ensure we're in the project root
if [ ! -f "pyproject.toml" ]; then
    echo "Error: Please run this script from the project root directory."
    exit 1
fi

# Test counter
tests_passed=0
tests_total=0

# Helper function to run a test
run_test() {
    tests_total=$((tests_total + 1))
    echo ""
    echo "Running Test $tests_total: $1"
    echo "------------------------------------------------"
    
    if uv run python -c "$2"; then
        echo "PASSED"
        tests_passed=$((tests_passed + 1))
    else
        echo "FAILED"
    fi
}

echo "Starting tests..."

# Test 1: Module Imports
run_test "Module Imports" '
from src.database import get_connection, create_schema, load_all_data
from src.queries import get_kpi_summary, get_category_performance, get_student_journey
from src.analysis import identify_key_opportunities, get_quiz_performance_issues
from src.utils import plot_category_performance, plot_engagement_trend
print("All modules imported successfully.")
'

# Test 2: Database Connection
run_test "Database Connection" '
from src.database import get_connection
conn = get_connection()
print("Database connection successful.")
conn.close()
'

# Test 3: KPI Summary
run_test "KPI Summary Query" '
from src.database import get_connection
from src.queries import get_kpi_summary
conn = get_connection()
df = get_kpi_summary(conn)
print(df)
conn.close()
'

# Test 4: Category Performance
run_test "Category Performance" '
from src.database import get_connection
from src.queries import get_category_performance
conn = get_connection()
df = get_category_performance(conn)
print(df.head())
conn.close()
'

# Test 5: Key Opportunities
run_test "Key Opportunities Analysis" '
from src.database import get_connection
from src.analysis import identify_key_opportunities
conn = get_connection()
df = identify_key_opportunities(conn)
print(df)
conn.close()
'

# Test 6: Full Pipeline Test
run_test "Full Pipeline Test" '
from src.database import get_connection, create_schema, load_all_data
from src.queries import get_kpi_summary, get_student_journey
conn = get_connection()
create_schema(conn)
load_all_data(conn)
print("KPI:", get_kpi_summary(conn).shape)
print("Journey:", get_student_journey(conn).shape[0], "rows")
conn.close()
print("Full pipeline test completed.")
'

echo ""
echo "================================================================"
echo "Test Summary: $tests_passed / $tests_total tests passed"
echo "================================================================"

if [ $tests_passed -eq $tests_total ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "Some tests failed. Please check the output above."
    exit 1
fi