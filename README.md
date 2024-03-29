# UrbanTide Technical Task

## Overview
This application ingests, validates and inserts data into a containerised SQL database. It involves a Flask-based web API that processes data from CSV files with a specific format (timestamp, value, category), infers the SQL table structure, performs basic outlier detection and populates a PostgreSQL database if the data passes the validation checks. The application is dockerised for easy setup and deployment. In line with best development practices, the code is PEP 8 compliant, verified using Flake8 to ensure high standards of code quality.

## Technologies Used
* **Python**: Core language for the backend.  
* **Flask**: Web framework for the API.  
* **PostgreSQL**: SQL database for data storage.  
* **Docker**: Containerisation of the application and database.  

## Setup Instructions
1. Clone this repository to your local machine.
2. Ensure that Docker is installed on your system.
3. Build the containers by navigating into the project directory and running the following command:
```bash
docker-compose up --build
```
4. **Important Note for macOS users:** The application uses port 5000, which may conflict with AirPlay. If you have issues with the port, you may need to deactivate AirPlay or change the port in the docker-compose.yml file.

## Using the application
To use the application, you can send a POST request with a CSV file to http://localhost:5000/upload-csv once the Docker containers are running. This can be done using tools such as Insomnia or Postman. If you decide to use Insomnia like I did, make sure you select the option 'Multipart' with 'file' as name and the CSV file as value. Alternatively, on Postman, under Body, make sure you select 'form-data' and create a new key named 'file' with the CSV file as value. You can test the application by using the test1.csv and test2.csv found in the Data folder. 

If you upload test1.csv, you should get a 200 OK message. If you upload test2.csv, you should get an error message as the file contains an outlier value of 100. If the file uploaded is not .CSV, empty, missing required columns or if no file at all is uploaded, you should see appropriate error messages. Note: The other CSV files in the Data folder have been created merely for testing purposes. To verify that the data generated from test1.csv has been inserted properly into the containerised database, you can run the following commands:
```bash
docker exec -it urban-tide-technical-task-postgres-1 bash
``` 
```bash
psql -U postgres
```  
Once inside the containerised PostgreSQL database, run the following to display the inserted data:
```sql
SELECT * FROM test;
```

## Testing
In order to ensure that the application works as intended, a series of automated tests have been provided. You can follow these steps to run the tests locally:

1. Create and activate virtual environment: Run ```python -m venv venv``` and ```source venv/bin/activate```. Make sure that all dependencies are installed correctly by running ```pip install -r src/requirements.txt```.
2. Set the Python Path: Set the PYTHONPATH environment variable to include 'src' so that Python can locate all necessary modules. In the root directory of the project, run ```export PYTHONPATH=./src```.
3. Run the tests: Use ```python -m pytest```. This will execute all test files located in the project's tests folder.

## Challenges
Throughout the development of this project, I encountered the following challenges:

* **Outlier Detection**: Choosing an effective method for detecting outliers required revisiting my Statistics notes from my master's, especially the Z-score. Even after settling on a method, adjusting the detection threshold (from 3 to 2.58) was necessary in order to correctly identify the outlier in test2.csv.
* **Mastering Docker**: Grasping the concept of Docker containers as well as learning how to use them was a bit challenging at first. After some initial trial and error, I understood that the data inserted into a Dockerised database via a POST request would not be found in my local database since they are two different locations.
* **Database Connections**: At first, I assumed that default settings would be enough for database connections. I soon realised that I needed to incorporate environment variables to the docker-compose.yml file if I wanted to easily transition between local and Dockerised environments.
* **Port 5000 on Macs**: I ran into a few issues at the start as port 5000 was occupied by Airplay on my Mac so my application could not run properly. I considered changing the application’s port but eventually decided to add a note to the README.md file simply advising macOS users to deactivate Airplay on their local machine.
* **Testing the /upload-csv Route**: Developing robust tests for the Flask API was a challenge as I had to both consider all the possible cases and errors (no file, non-CSV files, empty CSV files, CSV files with the wrong structure, CSV files with outliers, CSV files without outliers) and familiarise myself with the syntax required to test clients. After reviewing the Flask documentation and undertaking some independent research, I was able to successfully test the /upload-csv route.

## Contact
For any questions regarding this project, please reach out to Pablo Bravo Galindo at pablobgldo@gmail.com.
