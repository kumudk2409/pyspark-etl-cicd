# Base image containing Spark pre-installed
# Using Bitnami image for stability and security updates
FROM bitnami/spark:3.5.0

# Set working directory inside the container
WORKDIR /app

# Copy ETL application code
COPY etl/ etl/

# Copy Python dependencies
COPY requirements.txt .

# Install Python dependencies required for ETL
RUN pip install --no-cache-dir -r requirements.txt

# Default command executed by the container
# Spark Operator overrides this using spark-submit
CMD ["spark-submit", "etl/main.py"]