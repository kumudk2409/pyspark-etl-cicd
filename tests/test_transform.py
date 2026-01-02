"""
Unit tests for transformation logic.

These tests run in GitHub Actions during CI to ensure
data transformations behave as expected.
"""

from pyspark.sql import SparkSession
from etl.transform import clean_data


# Create a local Spark session for testing
spark = SparkSession.builder \
    .master("local") \
    .appName("PySparkUnitTests") \
    .getOrCreate()


def test_clean_data_filters_invalid_rows():
    """
    Verifies that:
    - Rows with null values are removed
    - Negative amounts are filtered out
    """

    # Sample test input
    data = [
        ("Alice", "10"),
        ("Bob", "-5"),
        ("Charlie", None)
    ]

    df = spark.createDataFrame(data, ["name", "amount"])

    # Apply transformation
    result = clean_data(df).collect()

    # Only one valid row should remain
    assert len(result) == 1
    assert result[0]["name"] == "Alice"