"""
Transformation logic for the ETL pipeline.

This module contains reusable and testable data transformation functions.
Keeping transformations separate from I/O makes unit testing easier.
"""

from pyspark.sql.functions import col


def clean_data(df):
    """
    Cleans and filters raw input data.

    Steps:
    1. Remove rows with null values
    2. Cast 'amount' column to double
    3. Filter out negative or zero amounts

    Args:
        df (DataFrame): Raw Spark DataFrame

    Returns:
        DataFrame: Cleaned Spark DataFrame
    """

    return (
        df.dropna()
          .withColumn("amount", col("amount").cast("double"))
          .filter(col("amount") > 0)
    )