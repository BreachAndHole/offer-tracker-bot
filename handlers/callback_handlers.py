from aiogram.types import Message
from bot import bot, dp


@dp.callback_query_handler(text='success_add_btn')
async def success_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


@dp.callback_query_handler(text='success_remove_btn')
async def success_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


@dp.callback_query_handler(text='cancel_btn')
async def cancel_changes(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'cancel')
