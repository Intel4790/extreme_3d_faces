```python
import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        raise Exception(f'Environment variable {var_name} not set')

def load_config():
    config = {
        'DB_HOST': get_env_variable('DB_HOST'),
        'DB_PORT': get_env_variable('DB_PORT'),
        'DB_USER': get_env_variable('DB_USER'),
        'DB_PASS': get_env_variable('DB_PASS'),
        'DB_NAME': get_env_variable('DB_NAME'),
    }
    return config
```