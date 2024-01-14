# UrbanTide Technical Task

## Overview
This application consumes, validates and inserts data into a containerised SQL database. It involves a Flask-based web API that processes data from CSV files with a specific format (timestamp, value, category), infers the appropriate SQL table structure, performs basic outlier detection and populates a PostgreSQL database if the the data passes the validation checks. The application is also dockerized for easy setup and deployment.

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
To use the application, you can send a POST request with a CSV file to http://localhost:5000/upload-csv once the Docker containers are running. This can be done using tools like Insomnia or Postman. If you decide to use Insomnia like I did, make sure to use 'Multipart form' with an entry with 'file' as name and the CSV file as value. You can test the application by using the CSV files found in the Data folder. If you upload test2.csv, you should get an error message as the file contains an outlier value of 100. If you upload test1.csv, you should receive a 200 OK success message. If the file uploaded is not .CSV, you should get an error message saying 'Invalid file format'.

To verify that the data generated from test1.csv has been inserted properly, you can run the following commands:
```bash
docker exec -it urban-tide-technical-task-postgres-1 bash
``` 
```bash
psql -U postgres
```  
Once inside the containerised PostgreSQL database, run the following to display the contents of the table with the inserted data:
```sql
SELECT * FROM test;
```  

## Contact
For any questions regarding this project, please reach out to Pablo Bravo Galindo at pablobgldo@gmail.com.
