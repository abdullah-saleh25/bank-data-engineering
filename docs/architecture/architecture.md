# Banking Data Platform Architecture

## Project Objective

Build a production-ready End-to-End Data Engineering pipeline for a banking system using Azure and Databricks.

---

## Data Sources

The platform ingests data from multiple sources:

- SQL Server Database
- CSV Files
- JSON Files
- Exchange Rate API

---

## Storage Layer

Azure Data Lake Storage Gen2

All raw data will be stored before processing.

---

## Processing Engine

Azure Databricks

PySpark will be used for:

- Data Ingestion
- Data Cleaning
- Data Transformation
- Data Validation
- Aggregation

---

## Medallion Architecture

Bronze Layer

- Raw Data

Silver Layer

- Cleaned Data

Gold Layer

- Business Ready Data

---

## Data Consumption

Power BI

Business users will consume Gold tables.

---

## Future Improvements

- Data Quality Framework
- Incremental Loading
- Delta Live Tables
- CI/CD
- Monitoring