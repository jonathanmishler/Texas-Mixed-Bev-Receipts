import psycopg2
from pgcopy import CopyManager

from config import Settings
from model import Receipt

settings = Settings()


def create_conn():
    DB_CONNECT = f"postgres://{settings.db_user}:{settings.db_password}@{settings.db_host}:5432/{settings.db_name}"
    return psycopg2.connect(DB_CONNECT)


def sql_col_def(name, props) -> str:
    """Creates the SQL column definitions for each property in the model schema"""
    col_type = props.get("type")
    if col_type == "string":
        # Pydantic uses type string for most JSON schema mapping and uses format for string sub-types
        if props.get("format") == "date-time":
            col_def = f"{name} TIMESTAMP"
        elif props.get("maxLength") is not None:
            col_def = f"{name} VARCHAR({props.get('maxLength')})"
        else:
            col_def = f"{name} VARCHAR(250)"
    elif col_type == "integer":
        col_def = f"{name} INTEGER"

    elif col_type == "boolean":
        col_def = f"{name} BOOLEAN"
    return col_def


def create_table_from_schema(schema: dict):
    # Create the SQL statement
    tbl_name = schema.get("db_table_name")
    cols = schema.get("properties")
    sql_columns = ",".join([sql_col_def(*item) for item in cols.items()])
    sql_table = f"CREATE TABLE IF NOT EXISTS {tbl_name}({tbl_name}_id SERIAL PRIMARY KEY,{sql_columns})"

    # Exectue SQL on database
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(sql_table)
    conn.commit()
    cursor.close()
