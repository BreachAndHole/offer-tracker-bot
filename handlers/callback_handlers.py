from aiogram import Dispatcher
from aiogram.types import Message

from services import database_services
from bot import bot
from config import callbacks


async def cancel_changes(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)


async def success_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='success', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Новая успешная встреча добавлена')


async def success_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='success', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Одна успешная встреча удалена')


async def postponed_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='postponed', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Новая перенесенная встреча добавлена')


async def postponed_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='postponed', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Одна перенесенная встреча удалена')


async def refused_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='refused', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Новый отказ добавлен')


async def refused_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='refused', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Одна отказ удален')


async def invite_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='invite_friend', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Приведи друга" добавлен')


async def invite_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='invite_friend', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Приведи друга" удалён')


async def transfer_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='transfer_abroad', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Перевод за рубеж" добавлен')


async def transfer_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='transfer_abroad', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Перевод за рубеж" удалён')


async def mobile_bank_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='mobile_bank', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Мобильный банк" добавлен')


async def mobile_bank_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='mobile_bank', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Мобильный банк" удалён')


async def debit_card_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='debit_card', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Дебетовая карта" добавлен')


async def debit_card_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='debit_card', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Дебетовая карта" удалён')


async def credit_card_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='credit_card', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Кредитная карта" добавлен')


async def credit_card_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='credit_card', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Кредитная карта" Удалён')


async def sim_card_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='sim_card', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф Мобайл" добавлен')


async def sim_card_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='sim_card', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф Мобайл" удалён')


async def investments_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='investments', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф инвестиции" добавлен')


async def investments_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='investments', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф инвестиции" удалён')


async def junior_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='junior', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф джуниор" добавлен')


async def junior_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='junior', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф джуниор" удалён')


async def subscription_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='subscription', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Подписка Pro" добавлен')


async def subscription_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='subscription', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Подписка Pro" удалён')


async def card_protection_add(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='card_protection', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Защита карты" добавлен')


async def card_protection_remove(message: Message):
    database_services.change_result_field(message.from_user.id, field_name='card_protection', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Защита карты" удалён')


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(cancel_changes, text=callbacks.CANCEL)
    dp.register_callback_query_handler(success_add, text=callbacks.SUCCESS_ADD)
    dp.register_callback_query_handler(success_remove, text=callbacks.SUCCESS_REMOVE)
    dp.register_callback_query_handler(postponed_add, text=callbacks.POSTPONED_ADD)
    dp.register_callback_query_handler(postponed_remove, text=callbacks.POSTPONED_REMOVE)
    dp.register_callback_query_handler(refused_add, text=callbacks.REFUSED_ADD)
    dp.register_callback_query_handler(refused_remove, text=callbacks.REFUSED_REMOVE)
    dp.register_callback_query_handler(invite_add, text=callbacks.INVITE_FRIEND_ADD)
    dp.register_callback_query_handler(invite_remove, text=callbacks.INVITE_FRIEND_REMOVE)
    dp.register_callback_query_handler(transfer_add, text=callbacks.TRANSFER_ABROAD_ADD)
    dp.register_callback_query_handler(transfer_remove, text=callbacks.TRANSFER_ABROAD_REMOVE)
    dp.register_callback_query_handler(mobile_bank_add, text=callbacks.MOBILE_BANK_ADD)
    dp.register_callback_query_handler(mobile_bank_remove, text=callbacks.MOBILE_BANK_REMOVE)
    dp.register_callback_query_handler(debit_card_add, text=callbacks.DEBIT_CARD_ADD)
    dp.register_callback_query_handler(debit_card_remove, text=callbacks.DEBIT_CARD_REMOVE)
    dp.register_callback_query_handler(credit_card_add, text=callbacks.CREDIT_CARD_ADD)
    dp.register_callback_query_handler(credit_card_remove, text=callbacks.CREDIT_CARD_REMOVE)
    dp.register_callback_query_handler(sim_card_add, text=callbacks.SIM_CARD_ADD)
    dp.register_callback_query_handler(sim_card_remove, text=callbacks.SIM_CARD_REMOVE)
    dp.register_callback_query_handler(investments_add, text=callbacks.INVESTMENTS_ADD)
    dp.register_callback_query_handler(investments_remove, text=callbacks.INVESTMENTS_REMOVE)
    dp.register_callback_query_handler(junior_add, text=callbacks.JUNIOR_ADD)
    dp.register_callback_query_handler(junior_remove, text=callbacks.JUNIOR_REMOVE)
    dp.register_callback_query_handler(subscription_add, text=callbacks.SUBSCRIPTION_ADD)
    dp.register_callback_query_handler(subscription_remove, text=callbacks.SUBSCRIPTION_REMOVE)
    dp.register_callback_query_handler(card_protection_add, text=callbacks.CARD_PROTECTION_ADD)
    dp.register_callback_query_handler(card_protection_remove, text=callbacks.CARD_PROTECTION_REMOVE)
