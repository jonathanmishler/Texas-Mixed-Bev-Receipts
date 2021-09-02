import psycopg2
from pgcopy import CopyManager
from sqlmodel import SQLModel, create_engine, Session
from config import Settings
import models  # noqa


settings = Settings()
DB_URL = f"postgres://{settings.db_user}:{settings.db_password}@{settings.db_host}:5432/{settings.db_name}"
engine = create_engine(DB_URL, echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
