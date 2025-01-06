import os

# Load in database configurations
DB_CONFIG = {
    'user': os.getenv('DB_USER', 'root'),         
    'password': os.getenv('DB_PASSWORD', 'root'),  
    'host': os.getenv('DB_HOST', '127.0.0.1'),     
    'database': os.getenv('DB_NAME', 'testing')    
}
