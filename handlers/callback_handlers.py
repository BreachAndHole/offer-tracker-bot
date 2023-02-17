from aiogram import Dispatcher
from aiogram.types import Message

import database
from bot import bot
from keyboards.buttons_config import inline_buttons


async def cancel_changes(message: Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)


async def success_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='success', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Новая успешная встреча добавлена')


async def success_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='success', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Одна успешная встреча удалена')


async def postponed_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='postponed', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Новая перенесенная встреча добавлена')


async def postponed_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='postponed', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Одна перенесенная встреча удалена')


async def refused_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='refused', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Новый отказ добавлен')


async def refused_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='refused', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Одна отказ удален')


async def invite_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='invite_friend', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Приведи друга" добавлен')


async def invite_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='invite_friend', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Приведи друга" удалён')


async def transfer_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='transfer_abroad', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Перевод за рубеж" добавлен')


async def transfer_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='transfer_abroad', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Перевод за рубеж" удалён')


async def mobile_bank_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='mobile_bank', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Мобильный банк" добавлен')


async def mobile_bank_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='mobile_bank', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Мобильный банк" удалён')


async def debit_card_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='debit_card', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Дебетовая карта" добавлен')


async def debit_card_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='debit_card', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Дебетовая карта" удалён')


async def credit_card_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='credit_card', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Кредитная карта" добавлен')


async def credit_card_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='credit_card', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Кредитная карта" Удалён')


async def sim_card_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='sim_card', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф Мобайл" добавлен')


async def sim_card_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='sim_card', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф Мобайл" удалён')


async def investments_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='investments', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф инвестиции" добавлен')


async def investments_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='investments', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф инвестиции" удалён')


async def junior_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='junior', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф джуниор" добавлен')


async def junior_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='junior', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Тинькофф джуниор" удалён')


async def subscription_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='subscription', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Подписка Pro" добавлен')


async def subscription_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='subscription', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Подписка Pro" удалён')


async def card_protection_add(message: Message):
    database.change_result_field(message.from_user.id, field_name='card_protection', is_increment=True)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Защита карты" добавлен')


async def card_protection_remove(message: Message):
    database.change_result_field(message.from_user.id, field_name='card_protection', is_increment=False)
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 'Оффер "Защита карты" удалён')


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(cancel_changes, text=inline_buttons.cancel)
    dp.register_callback_query_handler(success_add, text=inline_buttons.success.add)
    dp.register_callback_query_handler(success_remove, text=inline_buttons.success.remove)
    dp.register_callback_query_handler(postponed_add, text=inline_buttons.postponed.add)
    dp.register_callback_query_handler(postponed_remove, text=inline_buttons.postponed.remove)
    dp.register_callback_query_handler(refused_add, text=inline_buttons.refused.add)
    dp.register_callback_query_handler(refused_remove, text=inline_buttons.refused.remove)
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
    dp.register_callback_query_handler(card_protection_add, text=inline_buttons.card_protection.add)
    dp.register_callback_query_handler(card_protection_remove, text=inline_buttons.card_protection.remove)
