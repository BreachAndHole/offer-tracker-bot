from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

import config
import database
from database import BotUser


bot = Bot(token=config.API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: Message):
    user = BotUser(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    is_new_user = database.add_user_to_database(user)
    if is_new_user:
        await bot.send_message(
            chat_id=config.ADMIN_ID,
            text=f'New user added: {user.first_name} {user.last_name}'
        )

    await message.delete()
    await message.answer('/start, /help - Вызвать меню и справку')


@dp.message_handler()
async def echo(message: Message):
    await message.delete()
    await message.answer(f'This is an echo to {message.text=}')


if __name__ == '__main__':
    database.create_database()
    executor.start_polling(dp, skip_updates=True)
