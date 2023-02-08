import sqlite3
import queries
from dataclasses import dataclass
from config import DB_FILE_NAME


@dataclass
class BotUser:
    telegram_id: int
    first_name: str
    last_name: str


@dataclass
class DailyResult:
    # Meetings
    user_id: int
    success: int
    postponed: int
    canceled: int

    # Offers
    invite_friend: int
    transfer_abroad: int
    mobile_bank: int
    debit_card: int
    credit_card: int
    sim_card: int
    investments: int
    junior: int
    subscription: int


def execute_query(query: str, file_name=DB_FILE_NAME) -> None:
    with sqlite3.connect(DB_FILE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()


def execute_read_query(query: str, file_name=DB_FILE_NAME) -> list[tuple]:
    with sqlite3.connect(DB_FILE_NAME) as connection:
        cursor = connection.cursor()
        result = cursor.execute(query).fetchall()
        cursor.close()
    return result


def create_database(file_name=DB_FILE_NAME) -> None:
    execute_query(queries.CREATE_USER_TABLE)
    execute_query(queries.CREATE_RESULT_TABLE)


def get_all_user_ids(file_name=DB_FILE_NAME) -> list[int]:
    query_result = execute_read_query(queries.GET_ALL_USER_IDS)
    ids = [user_id for user_id, in query_result]
    return ids


def user_is_in_database(bot_user: BotUser, file_name=DB_FILE_NAME) -> bool:
    user_ids = get_all_user_ids()
    return bot_user.telegram_id in user_ids


def add_user_to_database(bot_user: BotUser, file_name=DB_FILE_NAME) -> bool:
    """ Adding user to database. Return True if it's a new user """
    if user_is_in_database(bot_user):
        return False

    query = f'''
        INSERT INTO bot_user (id, first_name, last_name)
        VALUES (
            {bot_user.telegram_id}, 
            "{bot_user.first_name}", 
            "{bot_user.last_name}"
        );
    '''
    execute_query(query)
    return True
