import sqlite3
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
