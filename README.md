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
3. Build the containers by navigating into the project directory and running ```docker-compose up --build```.

## Using the application
To use the application, you can send a POST request with a CSV file to http://localhost:5000/upload-csv once the Docker containers are running. This can be done using tools like Insomnia or Postman. If you decide to use Insomnia like I did, make sure to use 'Multipart form' with an entry with 'file' as name and the CSV file as value. You can test the application by using the CSV files found in the Data folder. If you upload test2.csv, you should receive a message saying 'File not uploaded - Outliers' as the file contains an outlier value of 100. If you upload test1.csv, you should receive a message saying 'File successfully uploaded'. If the file uploaded is not .CSV, you should see a message saying 'Invalid file format'.

To verify that the data has been inserted properly into the containerised PostgreSQL database, you can run ```docker exec -it urban-tide-technical-task-postgres-1 bash```, connect to the containerised database using ```psql -U postgres``` and run ```SELECT * FROM test``` to display the contents of the table where the data has been inserted.

## Functionality
CSV Upload: Accepts CSV files with a specific format (timestamp, value, category).  
Data Validation: Checks for outliers in the value field.  
Data Insertion: Data is inserted into the database if no outliers are detected. The table structure is inferred from the CSV content.

## Contact
For any questions regarding this project, please reach out to Pablo Bravo Galindo at pablobgldo@gmail.com.
