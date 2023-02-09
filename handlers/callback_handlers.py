from aiogram import Dispatcher, Bot
from aiogram.types import Message
from bot import bot


async def success_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def success_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def cancel_changes(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'cancel')


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(success_add, text='success_add_btn')
    dp.register_callback_query_handler(success_remove, text='success_remove_btn')
    dp.register_callback_query_handler(cancel_changes, text='cancel_btn')
