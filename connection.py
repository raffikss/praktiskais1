import mysql.connector
from mysql.connector import Error

# DB configs
import os

# DB configs loaded from environment variables
config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'root'),
    'host': os.getenv('DB_HOST', '127.0.0.1'),
    'database': os.getenv('DB_NAME', 'testing')
}

def create_connection(config):
    """Create a database connection using the given config."""
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
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
        print(f"Error reading data: {e}")
    finally:
        cursor.close()

def migrate_database(connection):
    "database migration by creating a users table."
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
        
        migration_query = """
        CREATE TABLE IF NOT EXISTS new_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(migration_query)
        print("Migration successful: new_table is created.")
        
    except Error as e:
        print(f"Error during migration: {e}")
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
    except Error as e:
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()

def insert_user_data(connection):
    "Insert user data into the users table interactively."
    try:
        cursor = connection.cursor()
        while True:
            user_name = input("Enter user name (or type 'exit' to stop): ")  # entering the user name
            if user_name.lower() == 'exit':
                break  # Exits the loop if 'exit' is typed

            user_status = input("Enter user status (active/inactive): ")  # Prompt for user activity

            # Check if the status is valid
            if user_status not in ['active', 'inactive']:
                print("Invalid status. Please enter 'active' or 'inactive'.")
                continue  # Ask for an input again

            # Insertomg the user data into the DB
            insert_query = "INSERT INTO users (user_name, user_status) VALUES (%s, %s)"
            cursor.execute(insert_query, (user_name, user_status))
            connection.commit()  # Commits the changes
            print("User data inserted successfully.")
    except Error as e:
        print(f"Error inserting user data: {e}")
    finally:
        cursor.close()

def main():
    # Establishing DB connection
    connection = create_connection(config)

    if connection:
        # Performomg DB migration 
        migrate_database(connection)



        # Readomg the current data from DB
        read_data(connection)

        # Allowing the user to insert new user data
        insert_user_data(connection)

        # Reading data again to show the new records
        print("Updated user records:")
        read_data(connection)

        # Close connection
        connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()  # Executes the main function
