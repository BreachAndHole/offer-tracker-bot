from aiogram import Bot, Dispatcher, executor
import config
import database
from handlers import message_handlers, callback_handlers
from bot import bot


if __name__ == '__main__':
    database.create_database()

    dp = Dispatcher(bot)
    message_handlers.setup(dp)
    callback_handlers.setup(dp)

    executor.start_polling(dp, skip_updates=True)
