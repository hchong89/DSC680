# Big Data Machine Learning Pipeline

## Overview
This project demonstrates an end-to-end big data and machine learning workflow using multiple tools within the Hadoop ecosystem. The pipeline ingests data into HDFS, structures the data using Hive, applies machine learning using Spark MLlib, and stores evaluation metrics into HBase.

The project validates distributed storage, SQL-based processing, machine learning workflows, and NoSQL database integration using scalable big data technologies.

---

## Technologies Used
- Apache NiFi
- HDFS
- Hive
- Apache Spark
- Spark MLlib
- HBase
- YARN
- Python

---

## Dataset
The dataset used in this project contains sleep-related variables including:
- Body weight
- Brain weight
- Maximum life span
- Gestation time
- Predation index
- Sleep exposure index
- Danger index
- Total sleep time

The dataset contained missing values and inconsistent entries, which were cleaned during preprocessing before machine learning modeling.

---

## Project Objectives
- Automate ingestion of data into HDFS using NiFi
- Create Hive tables and load structured data
- Build a distributed machine learning pipeline using Spark MLlib
- Store machine learning metrics into HBase
- Validate distributed execution using YARN logs
- Demonstrate integration across Hadoop ecosystem tools

---

## Pipeline Workflow

### 1. Data Ingestion with Apache NiFi
Apache NiFi was used to automate ingestion of the dataset into HDFS using:
- InvokeHTTP
- UpdateAttribute
- PutHDFS

The workflow downloaded the dataset from GitHub, standardized the filename, and stored the data inside HDFS for downstream processing.

---

### 2. Distributed Storage with HDFS
The dataset was uploaded into HDFS and validated using HDFS commands.

Example commands:
```bash
hdfs dfs -mkdir -p /tmp
hdfs dfs -put -f /tmp/dataset_2191_sleep.csv /tmp/
hdfs dfs -ls /tmp
```

---

### 3. Hive Table Creation
Hive was used to structure the dataset and support SQL-style querying.

The schema included:
- DOUBLE fields for continuous variables
- INT fields for categorical indexes
- STRING fields for columns containing missing value symbols ("?")

Aggregation queries and validation queries were performed after loading the dataset.

---

### 4. Spark Machine Learning Pipeline
Spark MLlib was used to:
- Load data directly from Hive
- Clean missing values
- Assemble feature vectors
- Split training and testing datasets
- Train a Random Forest Regressor
- Evaluate model performance

The model was designed to predict total sleep time using biological and behavioral variables.

---

### 5. HBase NoSQL Storage
HBase was used to store machine learning evaluation metrics including:
- RMSE
- R2

A timestamp-based row key was implemented to avoid overwriting previous model runs and allow historical comparisons.

Example commands:
```bash
create 'sleep_metrics', 'metrics'

put 'sleep_metrics', 'model1', 'metrics:rmse', '3.22'

put 'sleep_metrics', 'model1', 'metrics:r2', '0.405'

scan 'sleep_metrics'
```

---

### 6. YARN Monitoring
YARN logs were used to verify distributed Spark execution and monitor cluster processing behavior.

---

## Machine Learning Results

### Random Forest Regressor Results
- RMSE: 3.22
- R2: 0.405

The Random Forest model explained approximately 40.5% of the variance in total sleep time.

The model was selected because it can capture nonlinear relationships and feature interactions without strict assumptions required by linear regression models.

---

## Challenges Encountered
Several technical issues were encountered during development, including:
- HDFS path errors
- Spark syntax errors
- Dependency installation issues
- Library compatibility problems

These issues were resolved through:
- log debugging
- file path verification
- package reinstallation
- Spark job resubmission

---

## Key Skills Demonstrated
- Distributed data processing
- Hadoop ecosystem integration
- Spark MLlib workflows
- NoSQL database integration
- Data engineering pipelines
- Workflow automation
- Machine learning evaluation
- Big data infrastructure management

---

## Files Included
- `HDFS_Hive_Spark_Hbase.docx`
- `sleep_ml.py`
- `screenshots/`

---

## Future Improvements
Potential future enhancements include:
- Hyperparameter tuning
- Additional machine learning models
- Kafka streaming integration
- Real-time data ingestion
- Dashboard visualization of model outputs
- Cloud deployment using distributed infrastructure

```
