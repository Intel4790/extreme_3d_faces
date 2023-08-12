import os
from src.config import get_config
from src.utils import connect_to_db

def main():
    config = get_config()
    db_connection = connect_to_db(config['DB_URI'])
    
    # Add your application logic here

if __name__ == "__main__":
    main()