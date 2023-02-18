import sqlite3
from config import queries
from config.basic import DB_FILE_NAME


def execute_query(query: str) -> None:
    with sqlite3.connect(DB_FILE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()


def execute_read_query(query: str) -> list[tuple]:
    with sqlite3.connect(DB_FILE_NAME) as connection:
        cursor = connection.cursor()
        result = cursor.execute(query).fetchall()
        cursor.close()
    return result


def create_database() -> None:
    execute_query(queries.CREATE_RESULT_TABLE)
