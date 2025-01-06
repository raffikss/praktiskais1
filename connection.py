from config import DB_CONFIG  # Imports the configuration dictionary
from db_inserter import DBInserter
import mysql.connector
from mysql.connector import Error
from log_setup import logger

def create_connection(config):
    """Create a database connection using the given config."""
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            logger.info("Successfully connected to the database.")
            return connection
    except Error as e:
        logger.error(f"Error while connecting to MySQL: {e}")
        return None

def read_data(connection):
    """Read data from the 'users' table and print each record."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_status = 'active'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        logger.error(f"Error reading data: {e}")
    finally:
        cursor.close()

def migrate_database(connection):
    """Database migration by creating a users table."""
    try:
        cursor = connection.cursor()
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_status VARCHAR(50) NOT NULL
        )
        """
        cursor.execute(create_users_table_query)
        print("Migration successful: users table is created.")
        logger.info("Migration successful: users table is created.")
        
        migration_query = """
        CREATE TABLE IF NOT EXISTS new_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(migration_query)
        logger.info("Migration successful: new_table is created.")
        
    except Error as e:
        logger.error(f"Error during migration: {e}")
    finally:
        cursor.close()

def main():
    # Establishing DB connection
    connection = create_connection(DB_CONFIG)

    if connection:
        # Performs DB migration
        migrate_database(connection)

        # Reads current data from DB
        read_data(connection)

        # Create an instance of DBInserter 
        inserter = DBInserter(connection)
        
        # Inserts test data
        inserter.insert_test_data()

        # Allow the user to insert new user data manually
        inserter.insert_user_data()

        # Re-reading data again refreh records
        logger.info("Updated user records:")
        read_data(connection)

        # Closes connection
        connection.close()
        logger.info("Database connection closed.")

if __name__ == "__main__":
    main()
