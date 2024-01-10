from flask import Flask, request, jsonify
from utils import process_csv, infer_data_types, detect_outliers

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
        data_types = infer_data_types(df)
        print(detect_outliers(df))
        return jsonify({'message': 'File successfully uploaded'}), 200
    else:
        return jsonify({'error': 'Invalid file format'}), 400
    
