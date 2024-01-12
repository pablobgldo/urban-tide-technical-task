import pandas as pd


# Reads CSV file and converts it into DataFrame.
def process_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        # Converts 'timestamp' column in Dataframe to datetime object.
        # Not dynamic as code only works if there's a column 'timestamp'.
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except Exception as e:
        raise ValueError(f"Error processing CSV file: {e}")


# Takes DataFrame and returns dict with column (key) and SQL data type (value).
def infer_data_types(df):
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


# Detects outliers in a DataFrame using Z-score method.
# Returns empty Dataframe if no outliers found.
def detect_outliers(df, threshold=2.58):
    # Tried threshold of 3 but did not find outlier 100 so lowered it to 2.58.
    outliers = pd.DataFrame()
    # Performs outlier detection only on columns with numerical values.
    for column in df.select_dtypes(include=['number']):
        # Calculates Z-score for each value in column.
        df['z_score'] = (df[column] - df[column].mean()) / df[column].std()
        # Appends Z-score to 'outliers' if Z-score is higher than threshold.
        outliers = outliers._append(df[df['z_score'].abs() > threshold])
    return outliers
