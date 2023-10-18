# Real-Time Data Streaming and Processing with Apache Spark

## Overview
This project demonstrates the end-to-end process of real-time data streaming and processing, combining the power of popular tools like Apache Kafka, Apache Spark, Apache Cassandra, and Apache Airflow. It leverages real-time weather data from a public API and showcases a streamlined data engineering pipeline.

### Project Highlights
- Data source: Real-time weather data retrieved from a Weather API.
- Automation: Apache Airflow is used for scheduling and automating data fetching.
- Data Streaming: Data is pushed to Apache Kafka in real time.
- Data Processing: Apache Spark processes and transforms the data.
- Data Storage: Processed data is stored in an Apache Cassandra database.
- Dashboard: Visualize the data in Cassandra using your preferred tool.

## Project Structure
- `kafka_stream.py`: Contains the Python scripts for fetching real-time data using the Weather API and Apache Airflow DAGs to automate the process.
- `spark_streams`: Includes the Apache Spark application to subscribe to the Kafka topic, process data, and load it into Apache Cassandra.
- `docker-compose.yml`: Provides a Docker Compose configuration for setting up your development environment, including Kafka, Cassandra, and Spark.

## Prerequisites
- Python 3.x
- Apache Airflow
- Apache Kafka
- Apache Spark
- Apache Cassandra
- Docker and Docker Compose (for local development)

## Getting Started
1. Clone this repository to your local machine.
2. Install the required dependencies and set up your environment.
3. Configure your credentials for Apache Airflow in the Postgres database.
4. Start the services using Docker Compose.
5. Run the Airflow DAGs to fetch real-time data.
6. Execute the Apache Spark application to process the data and store it in Cassandra.

## Usage
- Customize the data source or adapt the project for your specific use case.
- Develop your data visualization or analysis tools to interact with the Cassandra database.
- Extend the project by adding more data sources, processors, or analytics.
