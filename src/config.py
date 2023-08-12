```python
import os

# Database configuration
DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432),
    'user': os.getenv('DB_USER', 'user'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'database')
}

# Application configuration
APP_CONFIG = {
    'log_level': os.getenv('LOG_LEVEL', 'INFO'),
}
```