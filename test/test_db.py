from src.db import create_table, insert_data
import unittest
from unittest import mock


class TestDbFunctions(unittest.TestCase):

    def test_create_table(self):
        conn_mock = mock.MagicMock()
        cursor_mock = conn_mock.cursor.return_value

        dtypes = {'col1': 'INT', 'col2': 'VARCHAR'}
        table_name = 'test'
        query = 'CREATE TABLE IF NOT EXISTS test (col1 INT, col2 VARCHAR);'
        create_table(conn_mock, table_name, dtypes)

        cursor_mock.execute.assert_called_with(query)
        conn_mock.commit.assert_called_once()
        cursor_mock.close.assert_called_once()

    def test_insert_data(self):
        conn_mock = mock.MagicMock()
        cursor_mock = conn_mock.cursor.return_value

        df_mock = mock.MagicMock()
        df_mock.columns = ['col1', 'col2']
        df_mock.itertuples.return_value = [(1, '1'), (2, '2')]
        query = 'INSERT INTO test (col1, col2) VALUES (%s, %s)'
        calls = [mock.call(query, (1, '1')), mock.call(query, (2, '2'))]
        insert_data(conn_mock, 'test', df_mock)

        cursor_mock.execute.assert_has_calls(calls)
        conn_mock.commit.assert_called_once()
        cursor_mock.close.assert_called_once()
