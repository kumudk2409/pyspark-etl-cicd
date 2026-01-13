PySpark ETL CI/CD on Kubernetes
--------------------------------
A production-style, end‑to‑end Big Data ETL project demonstrating how to build, test, containerize, and deploy a PySpark ETL pipeline on Kubernetes using Helm and GitHub Actions.

Project Overview
---------------------------------
The pipeline performs a basic ETL workflow:
-Extract raw CSV data from S3 (or local storage)
-Transform the data using PySpark (cleaning & filtering)
-Load the processed data back to S3 in Parquet format
-Deploy the Spark job on Kubernetes using the Spark Operator
-Automate testing, container builds, and deployment via GitHub Actions

Architecture
---------------------------------
GitHub Repository
 └── GitHub Actions
      ├── CI: PySpark unit tests
      ├── Docker image build & push
      └── CD: Helm deployment
                |
                v
        Kubernetes Cluster
                |
          Spark Operator
                |
          PySpark ETL Job
                |
               S3

Repository Structure
---------------------------------
pyspark-etl-cicd/
├── etl/                    # PySpark ETL application
│   ├── main.py             # ETL entry point
│   ├── transform.py        # Data transformation logic
│   └── __init__.py
├── tests/                  # Unit tests for ETL logic
│   └── test_transform.py
├── docker/                 # Docker image definition
│   └── Dockerfile
├── helm/                   # Helm chart for SparkApplication
│   └── pyspark-etl/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           └── sparkapplication.yaml
├── .github/
│   └── workflows/
│       └── cicd.yaml       # GitHub Actions CI/CD pipeline
├── requirements.txt        # Python dependencies
└── README.md

ETL Logic
--------------------------------------
Transformations Performed:-
-Drop rows with null values
-Cast amount column to numeric type
-Filter out negative or zero values

The transformation logic is isolated in a separate module to enable unit testing and reusability.

Docker Image
-------------------------------------
-Based on bitnami/spark:3.5.0
-Bundles PySpark ETL code and dependencies
-Built and pushed automatically by GitHub Actions

This image is used by the Spark Operator to run the job on Kubernetes.

 Kubernetes Deployment

Spark Operator
----------------------------------
The project uses the Spark Operator to run Spark jobs natively on Kubernetes using the SparkApplication CRD.

Helm
----------------------------------
Helm is used to:
-Template SparkApplication YAML
-Manage configuration via values files
-Enable repeatable, versioned deployments

CI/CD Pipeline (GitHub Actions)
---------------------------------
Pipeline Stages
1.CI Stage
-Checkout code
-Install PySpark & dependencies
-Run unit tests

2.Build Stage
-Build Docker image
-Push image to Docker registry

3.CD Stage
-Deploy SparkApplication using Helm

The pipeline only deploys if tests pass successfully.

Why This Project Matters
------------------------------
This repository demonstrates:
-PySpark ETL development
-Testable data pipelines
-Dockerized Spark jobs
-Kubernetes-native Spark execution
-Helm-based deployments
-CI/CD automation with GitHub Actions

It mirrors real-world data platform engineering patterns in a compact, understandable format.

Possible Enhancements
------------------------------------
-Parameterize input/output paths via Helm values
-Add data quality checks
-Integrate Airflow or Argo Workflows
-Add IAM Roles for Service Accounts (IRSA)
-Add metrics & monitoring
-Multi-environment Helm deployments (dev/stage/prod)

Author
----------------------------
Kumud Kumari
Infrastructure / Platform Engineer

License
----------------------------
MIT License