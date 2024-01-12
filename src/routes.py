from flask import Flask, request, jsonify
from utils import process_csv, infer_data_types, detect_outliers
from db import get_conn, create_table, insert_data

app = Flask(__name__)

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.csv'):
        df = process_csv(file)
        dtypes = infer_data_types(df)
        outliers = detect_outliers(df)
        del df['z_score']
        
        if outliers.empty:
            try:
                conn = get_conn()
                create_table(conn, 'hello', dtypes)
                insert_data(conn, 'hello', df)
                print('Data has now been inserted as there are no outliers')
            except Exception as e:
                print('Data could not be inserted despite lack of outliers: {e}')
        else:
            print('We have detected outliers so data will not be inserted')


        return jsonify({'message': 'File successfully uploaded'}), 200
    else:
        return jsonify({'error': 'Invalid file format'}), 400
    
