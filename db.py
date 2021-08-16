import psycopg2
from pgcopy import CopyManager

from config import Settings

settings = Settings()

DB_CONNECT = f'postgres://{settings.db_user}:{settings.db_password}@{settings.db_host}:5432/{settings.db_name}'