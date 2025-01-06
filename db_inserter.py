from mysql.connector import Error
from log_setup import logger

class DBInserter:
    def __init__(self, connection):
        """
        Initialize the DBInserter with a database connection.
        :param connection: MySQL database connection object.
        """
        self.connection = connection

    def insert_test_data(self):
        """
        Inserts test data into the 'users' table, clearing existing data first.
        """
        try:
            cursor = self.connection.cursor()

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
            self.connection.commit()
            print("Test data inserted into users table.")
            logger.info("Test data inserted into users table.")
        except Error as e:
            logger.error(f"Error inserting test data: {e}")
        finally:
            cursor.close()

    def insert_user_data(self):
        """
        Insert user data into the 'users' table interactively.
        """
        try:
            cursor = self.connection.cursor()
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
                self.connection.commit()
                print("User data inserted successfully.")
                logger.info("User data inserted successfully.")
        except Error as e:
            logger.error(f"Error inserting user data: {e}")
        finally:
            cursor.close()
