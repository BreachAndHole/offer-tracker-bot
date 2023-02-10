from aiogram import Dispatcher, Bot
from aiogram.types import Message
from bot import bot
from keyboards.buttons_config import inline_buttons


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
    dp.register_callback_query_handler(cancel_changes, text=inline_buttons.cancel)
    dp.register_callback_query_handler(success_add, text=inline_buttons.success.add)
    dp.register_callback_query_handler(success_remove, text=inline_buttons.success.remove)
    dp.register_callback_query_handler(postponed_add, text=inline_buttons.postponed.add)
    dp.register_callback_query_handler(postponed_remove, text=inline_buttons.postponed.remove)
    dp.register_callback_query_handler(canceled_add, text=inline_buttons.canceled.add)
    dp.register_callback_query_handler(canceled_remove, text=inline_buttons.canceled.remove)
    dp.register_callback_query_handler(invite_add, text=inline_buttons.invite_friend.add)
    dp.register_callback_query_handler(invite_remove, text=inline_buttons.invite_friend.remove)
    dp.register_callback_query_handler(transfer_add, text=inline_buttons.transfer_abroad.add)
    dp.register_callback_query_handler(transfer_remove, text=inline_buttons.transfer_abroad.remove)
    dp.register_callback_query_handler(mobile_bank_add, text=inline_buttons.mobile_bank.add)
    dp.register_callback_query_handler(mobile_bank_remove, text=inline_buttons.mobile_bank.remove)
    dp.register_callback_query_handler(debit_card_add, text=inline_buttons.debit_card.add)
    dp.register_callback_query_handler(debit_card_remove, text=inline_buttons.debit_card.remove)
    dp.register_callback_query_handler(credit_card_add, text=inline_buttons.credit_card.add)
    dp.register_callback_query_handler(credit_card_remove, text=inline_buttons.credit_card.remove)
    dp.register_callback_query_handler(sim_card_add, text=inline_buttons.sim_card.add)
    dp.register_callback_query_handler(sim_card_remove, text=inline_buttons.sim_card.remove)
    dp.register_callback_query_handler(investments_add, text=inline_buttons.investments.add)
    dp.register_callback_query_handler(investments_remove, text=inline_buttons.investments.remove)
    dp.register_callback_query_handler(junior_add, text=inline_buttons.junior.add)
    dp.register_callback_query_handler(junior_remove, text=inline_buttons.junior.remove)
    dp.register_callback_query_handler(subscription_add, text=inline_buttons.subscription.add)
    dp.register_callback_query_handler(subscription_remove, text=inline_buttons.subscription.remove)
