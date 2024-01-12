from flask import Flask, request, jsonify
from utils import process_csv, infer_data_types, detect_outliers
from db import get_conn, create_table, insert_data, close_conn

app = Flask(__name__)


@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    # Returns a 400 message if no file part in request.
    if 'file' not in request.files:
        return jsonify({'Error': 'No file part'}), 400

    file = request.files['file']

    if file.filename.endswith('.csv'):
        # Reads CSV file and converts it into DataFrame.
        df = process_csv(file)
        # Infers SQL data types from DataFrame.
        dtypes = infer_data_types(df)
        # Detects outliers using Z-score and adds Z-score column to DF.
        outliers = detect_outliers(df)
        # Removes Z-score column from Dataframe as it is no longer necessary.
        del df['z_score']

        # Creates table (if it does not exist) and inserts data into it.
        # Returns 200 if data is uploaded and 400 if outliers are found.
        if outliers.empty:
            conn = get_conn()
            create_table(conn, 'test', dtypes)
            insert_data(conn, 'test', df)
            close_conn(conn)
            return jsonify({'Message': 'File successfully uploaded'}), 200
        else:
            return jsonify({'Message': 'File not uploaded - Outliers'}), 400

    else:
        # Returns a 400 message if a file other than .CSV is uploaded.
        return jsonify({'Error': 'Invalid file format'}), 400
