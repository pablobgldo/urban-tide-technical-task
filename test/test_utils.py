import pandas as pd
from src.utils import process_csv, infer_data_types, detect_outliers


def test_process_csv():
    df = process_csv("data/test3.csv")
    expected_df = pd.DataFrame({
        "timestamp": pd.to_datetime([
            "2022-01-01 00:00:00", "2022-01-01 01:00:00"
            ]),
        "value": [1, 2],
        "category": [3, 5]
    })
    unexpected_df = pd.DataFrame({
        "timestamp": pd.to_datetime([
            "2022-01-01 00:00:00", "2022-01-01 01:00:00"
            ]),
        "value": [1, 2],
        "category": [3, 100]
    })

    assert df.equals(expected_df)
    assert not df.equals(unexpected_df)


def test_infer_data_types():
    df = pd.DataFrame({
        'integers': [1, 2],
        'floats': [1.1, 2.2],
        'dates': pd.to_datetime(["2022-01-01", "2022-01-02"]),
        'strings': ["A", "B"]
    })
    expected_dtypes = {
        'integers': 'INT',
        'floats': 'FLOAT',
        'dates': 'TIMESTAMP',
        'strings': 'VARCHAR'
    }
    unexpected_dtypes = {
        'integers': 'FLOAT',
        'floats': 'INT'
    }

    assert infer_data_types(df) == expected_dtypes
    assert infer_data_types(df) != unexpected_dtypes


def test_detect_outliers_if_none():
    df = pd.DataFrame({
        'values': [10, 12, 11, 13, 9, 10, 14]
    })
    outliers = detect_outliers(df, threshold=2.58)

    assert outliers.empty


def test_detect_outliers_if_outliers_exist():
    df = pd.DataFrame({
        'values': [10, 12, 11, 13, 9, 10, 9, 10, 12, 180]  # 180 is an outlier
    })
    outliers = detect_outliers(df, threshold=2.58)

    assert not outliers.empty
    assert 180 in outliers['values'].values
