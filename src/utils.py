import pandas as pd

def process_csv(file_path):
    """
    Reads CSV file and converts it into a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Error processing CSV file: {e}")
    
def infer_sql_data_types(df):
    """
    Infers SQL data types from a DataFrame.
    """
    inferred_types = {}
    for column in df.columns:
        if pd.api.types.is_integer_dtype(df[column]):
            inferred_types[column] = "INTEGER"
        elif pd.api.types.is_float_dtype(df[column]):
            inferred_types[column] = "FLOAT"
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            inferred_types[column] = "DATETIME"
        else:
            inferred_types[column] = "VARCHAR"
    return inferred_types

def detect_outliers(df, z_score_threshold=3):
    """
    Detects outliers in a DataFrame using the Z-score method.
    """
    outliers = pd.DataFrame()
    for column in df.select_dtypes(include=[ 'float64', 'int64']):
        df['z_score'] = (df[column] - df[column].mean()) / df[column].std()
        outliers = outliers.append(df[df['z_score'].abs() > z_score_threshold])
    return outliers.drop(columns=['z_score'])
