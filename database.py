import sqlite3
import queries
from config import DB_FILE_NAME


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
    execute_query(queries.CREATE_USER_TABLE)
    execute_query(queries.CREATE_RESULT_TABLE)
