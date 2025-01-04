from config import DB_CONFIG  # Import the configuration dictionary
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
    "Database migration by creating a users table."
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
        print("Migration successful: new_table is created.")
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

def insert_test_data(connection):
    "Inserting some test data into the users table, clearing existing data first."
    try:
        cursor = connection.cursor()
        
        # Clear existing entries
        cursor.execute("DELETE FROM users;")
        
        # Insert new test data
        insert_query = """
        INSERT INTO users (user_name, user_status) VALUES
        ('Alice', 'active'),
        ('Bob', 'inactive'),
        ('Charlie', 'active');
        """
        cursor.execute(insert_query)
        connection.commit()
        print("Test data inserted into users table.")
        logger.info("Test data inserted into users table.")
    except Error as e:
        logger.error(f"Error inserting data: {e}")
    finally:
        cursor.close()

def insert_user_data(connection):
    "Insert user data into the users table interactively."
    try:
        cursor = connection.cursor()
        while True:
            user_name = input("Enter user name (or type 'exit' to stop): ")
            if user_name.lower() == 'exit':
                break

            user_status = input("Enter user status (active/inactive): ")
            if user_status not in ['active', 'inactive']:
                print("Invalid status. Please enter 'active' or 'inactive'.")
                continue

            insert_query = "INSERT INTO users (user_name, user_status) VALUES (%s, %s)"
            cursor.execute(insert_query, (user_name, user_status))
            connection.commit()
            print("User data inserted successfully.")
            logger.info("User data inserted successfully.")
    except Error as e:
        logger.error(f"Error inserting user data: {e}")
    finally:
        cursor.close()

def main():
    # Establishing DB connection
    connection = create_connection(DB_CONFIG)

    if connection:
        # Performing DB migration
        migrate_database(connection)

        # Reading the current data from DB
        read_data(connection)

        # Allowing the user to insert new user data
        insert_user_data(connection)

        # Reading data again to show the new records
        logger.info("Updated user records:")
        read_data(connection)

        # Close connection
        connection.close()
        logger.info("Database connection closed.")

if __name__ == "__main__":
    main()
