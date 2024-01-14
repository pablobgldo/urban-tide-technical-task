# UrbanTide Technical Task - Data Ingestion, Processing and Insertion

## Overview
This application consumes, validates and inserts data into a containerised SQL database. It involves a Flask-based web API that processes data from CSV files, infers the appropriate SQL table structure, performs basic outlier detection and populates a PostgreSQL database if the the data passes the validation checks. The application is also dockerized for easy setup and deployment.

## Technologies Used
Python: Core language for the backend.  
Flask: Web framework for the API.  
PostgreSQL: SQL database for data storage.  
Docker: Containerisation of the application and database.  

## Setup Instructions
1. Clone this repository to your local machine.
2. Ensure that Docker is installed on your system.
3. Build/run the containers by navigating into the project directory and running ```docker-compose up --build``` to build/start the containers.

## Using the application
To use the application, you can send a POST request with a CSV file to http://localhost:5000/upload-csv once the Docker containers are running. This can be done using tools like Postman or Insomnia. To verify that data has been inserted into the PostgreSQL database inside the Docker container, you can run ```docker exec -it [your_postgres_container_name] bash``` in the CLI. You can find more details on Docker containers using ```docker ps```.

Using the Application
To use the application, you can send a POST request with a CSV file to http://localhost:5000/upload-csv. This can be done using tools like Postman or cURL.

Example cURL command:

bash
Copy code
curl -X POST -F 'file=@path_to_your_csv.csv' http://localhost:5000/upload-csv
Functionality
CSV Upload: Accepts CSV files with a specific format (timestamp, value, category).
Data Validation: Checks for outliers in the value field.
Database Interaction: If no outliers are detected, the data is inserted into the PostgreSQL database. The schema of the table is dynamically inferred from the CSV content.
Development Insights
Challenges Faced:

Ensuring proper communication between Docker containers.
Dynamic inference of SQL data types from CSV content.
Handling outlier detection efficiently.
Solutions:

Utilized Docker networking features for seamless container interaction.
Developed a Python function to map pandas DataFrame dtypes to SQL data types.
Implemented a Z-score based method for outlier detection.
