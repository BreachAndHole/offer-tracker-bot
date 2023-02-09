from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

import database
import messages
from config import ADMIN_ID
from keyboards.buttons_config import main_kb_buttons
from keyboards import replyKeyboards, inlineKeyboards
from bot import bot


async def start_command(message: Message):
    user = database.BotUser(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )

    # Adding user to database if he is new and messaging about it to admin
    if database.add_user_to_database(user):
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=f'New user added: {user.first_name} {user.last_name}'
        )

    # Delete message and open main keyboard
    await message.delete()
    await message.answer(
        text=messages.START_MESSAGE,
        reply_markup=replyKeyboards.main_keyboard
    )


async def stat_command(message: Message):
    user = database.BotUser(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    daily_result = database.get_user_daily_result(user)
    reply_text = messages.form_stat_message(daily_result)
    await message.delete()
    await message.answer(reply_text)


async def success_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.success_kb
    )


def setup(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(stat_command, commands=['stat'])

    # Inline handlers
    dp.register_message_handler(success_menu, Text(equals=main_kb_buttons.success))
