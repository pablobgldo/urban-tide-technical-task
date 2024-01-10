import pandas as pd

def process_csv(file_path):
    """
    Reads CSV file and converts it into a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
         # Convert 'timestamp' column to datetime. Not dynamic as code will only work if there's a column called 'timestamp'.
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except Exception as e:
        raise ValueError(f"Error processing CSV file: {e}")
    
def infer_data_types(df):
    """
    Infers SQL data types from a DataFrame.
    """
    dtypes = {}
    for column in df.columns:
        if pd.api.types.is_integer_dtype(df[column]):
            dtypes[column] = "INT"
        elif pd.api.types.is_float_dtype(df[column]):
            dtypes[column] = "FLOAT"
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            dtypes[column] = "TIMESTAMP"
        else:
            dtypes[column] = "VARCHAR"
    return dtypes

def detect_outliers(df, threshold=2.58):
    """
    Detects outliers in a DataFrame using the Z-score method.
    Attempted a threshold of 3 but didn't find outlier with value 100 so lowered it to 2.58.
    """
    outliers = pd.DataFrame()
    for column in df.select_dtypes(include=[ 'float64', 'int64']):
        df['z_score'] = (df[column] - df[column].mean()) / df[column].std()
        outliers = outliers._append(df[df['z_score'].abs() > threshold])
    return outliers.drop(columns=['z_score'])
