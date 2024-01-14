# UrbanTide Technical Task

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
3. Build and start the containers by navigating into the project directory and running ```docker-compose up --build```.

## Using the application
To use the application, you can send a POST request with a CSV file to http://localhost:5000/upload-csv once the Docker containers are running. This can be done using tools like Postman or Insomnia. To verify that the data has been inserted into the containerised database, you can run ```docker exec -it [postgres_container_name] bash``` in the CLI. You can find more details on containers using ```docker ps```.

## Functionality
CSV Upload: Accepts CSV files with a specific format (timestamp, value, category).  
Data Validation: Checks for outliers in the value field.  
Data Insertion: If no outliers are detected, the data is inserted into the PostgreSQL database. The structure of the table is inferred from the CSV content.

## Contact
For any further queries or discussions regarding this project, please reach out to Pablo Bravo Galindo at pablobgldo@gmail.com.
