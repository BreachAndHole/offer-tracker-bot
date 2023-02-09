from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Main keyboard buttons
# Meeting results
success_btn = KeyboardButton(text='Успешные')
postponed_btn = KeyboardButton(text='Переносы')
canceled_btn = KeyboardButton(text='Отказы')
# Offers
invite_friends_btn = KeyboardButton(text='Пригласи друга')
transfer_abroad = KeyboardButton(text='Переводы за рубеж')
mobile_bank = KeyboardButton(text='Мобильный банк')
debit_card = KeyboardButton(text='Дебетовая карта')
credit_card = KeyboardButton(text='Кредитная карта')
sim_card = KeyboardButton(text='Тинькофф Мобайл')
investments = KeyboardButton(text='Инвестиции')
junior = KeyboardButton(text='Джуниор')
subscription = KeyboardButton(text='Подписка PRO')

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
main_keyboard.row(success_btn, postponed_btn, canceled_btn)
main_keyboard.row(invite_friends_btn, transfer_abroad, mobile_bank)
main_keyboard.row(debit_card, credit_card, sim_card)
main_keyboard.row(investments, junior, subscription)
