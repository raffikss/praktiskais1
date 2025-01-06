import pytest
from unittest.mock import MagicMock
from mysql.connector import Error
from connection import migrate_database, read_data

#DB Config for testing
TEST_DB_CONFIG = {
    "host": "localhost",
    "user": "test_user",
    "password": "test_password",
    "database": "test_db",
}

# Tests function  migrate_database
def test_migrate_database():
    mock_conn = MagicMock()
    migrate_database(mock_conn)
    mock_conn.cursor.return_value.execute.assert_called()

# Tests function read_data
def test_read_data():
    mock_conn = MagicMock()
    mock_conn.cursor.return_value.fetchall.return_value = [(1, "Alice", "active")]
    read_data(mock_conn)
    mock_conn.cursor.return_value.execute.assert_called_with("SELECT * FROM users WHERE user_status = 'active'")

#Entry point for testing
if __name__ == "__main__":
    pytest.main()
