import os

# Load database configurations from environment variables or provide defaults
DB_CONFIG = {
    'user': os.getenv('DB_USER', 'root'),          # Replace 'root' with your default username
    'password': os.getenv('DB_PASSWORD', 'root'),  # Replace 'root' with your default password
    'host': os.getenv('DB_HOST', '127.0.0.1'),     # Replace '127.0.0.1' with your default host
    'database': os.getenv('DB_NAME', 'testing')    # Replace 'testing' with your default database name
}
