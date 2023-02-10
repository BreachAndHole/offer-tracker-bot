from aiogram import Dispatcher, Bot
from aiogram.types import Message
from bot import bot


async def cancel_changes(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'cancel')


async def success_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def success_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def postponed_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def postponed_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def canceled_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def canceled_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def invite_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def invite_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def transfer_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def transfer_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def mobile_bank_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def mobile_bank_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def debit_card_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def debit_card_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def credit_card_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def credit_card_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def sim_card_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def sim_card_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def investments_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def investments_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def junior_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def junior_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


async def subscription_add(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success +1')


async def subscription_remove(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'success -1')


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(cancel_changes, text='cancel_btn')
    dp.register_callback_query_handler(success_remove, text='success_remove_btn')
    dp.register_callback_query_handler(success_add, text='success_add_btn')
    dp.register_callback_query_handler(postponed_add, text='postponed_add_btn')
    dp.register_callback_query_handler(postponed_remove, text='postponed_remove_btn')
    dp.register_callback_query_handler(canceled_add, text='canceled_add_btn')
    dp.register_callback_query_handler(canceled_remove, text='canceled_remove_btn')
    dp.register_callback_query_handler(invite_add, text='invite_add_btn')
    dp.register_callback_query_handler(invite_remove, text='invite_remove_btn')
    dp.register_callback_query_handler(transfer_add, text='transfer_add_btn')
    dp.register_callback_query_handler(transfer_remove, text='transfer_remove_btn')
    dp.register_callback_query_handler(mobile_bank_add, text='mobile_add_btn')
    dp.register_callback_query_handler(mobile_bank_remove, text='mobile_remove_btn')
    dp.register_callback_query_handler(debit_card_add, text='debit_add_btn')
    dp.register_callback_query_handler(debit_card_remove, text='debit_remove_btn')
    dp.register_callback_query_handler(credit_card_add, text='credit_add_btn')
    dp.register_callback_query_handler(credit_card_remove, text='credit_remove_btn')
    dp.register_callback_query_handler(sim_card_add, text='sim_add_btn')
    dp.register_callback_query_handler(sim_card_remove, text='sim_remove_btn')
    dp.register_callback_query_handler(investments_add, text='investments_add_btn')
    dp.register_callback_query_handler(investments_remove, text='investments_remove_btn')
    dp.register_callback_query_handler(junior_add, text='junior_add_btn')
    dp.register_callback_query_handler(junior_remove, text='junior_remove_btn')
    dp.register_callback_query_handler(subscription_add, text='subscription_add_btn')
    dp.register_callback_query_handler(subscription_remove, text='subscription_remove_btn')
