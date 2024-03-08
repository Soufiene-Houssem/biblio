import os
from dotenv import load_dotenv
from flask_caching import Cache

load_dotenv()

class Config:
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
    MYSQL_ROOT_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')

    SQLALCHEMY_DATABASE_URI = f"mysql://root:{MYSQL_ROOT_PASSWORD}@mysql:{MYSQL_PORT}/{MYSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


cache = Cache(config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://redis:6379/0'})
