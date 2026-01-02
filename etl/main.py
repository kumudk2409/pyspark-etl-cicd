"""
Main entry point for the PySpark ETL job.

This script:
1. Creates a Spark session
2. Reads raw input data from S3 (or HDFS/local)
3. Applies transformation logic
4. Writes the cleaned data back to S3 in parquet format

This file is executed by spark-submit inside Kubernetes.
"""

from pyspark.sql import SparkSession
from transform import clean_data


def main():
    """
    Orchestrates the ETL workflow.
    """

    # Create Spark session with application name
    spark = SparkSession.builder \
        .appName("SimplePySparkETL") \
        .getOrCreate()

    # Input and output locations
    # In real setups, these should come from environment variables
    input_path = "s3a://input-bucket/data.csv"
    output_path = "s3a://output-bucket/cleaned/"

    # Read raw CSV data
    df = spark.read \
        .option("header", True) \
        .csv(input_path)

    # Apply business transformations
    cleaned_df = clean_data(df)

    # Write transformed data in columnar format for analytics
    cleaned_df.write \
        .mode("overwrite") \
        .parquet(output_path)

    # Stop Spark session explicitly
    spark.stop()


if __name__ == "__main__":
    main()
