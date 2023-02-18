from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import buttons

# Results keyboard buttons
# Meeting results
success_btn = KeyboardButton(text=buttons.SUCCESS_BTN_TEXT)
postponed_btn = KeyboardButton(text=buttons.POSTPONED_BTN_TEXT)
refused_btn = KeyboardButton(text=buttons.REFUSED_BTN_TEXT)
# Offers
invite_friend_btn = KeyboardButton(text=buttons.INVITE_FRIEND_BTN_TEXT)
transfer_abroad_btn = KeyboardButton(text=buttons.TRANSFER_ABROAD_BTN_TEXT)
mobile_bank_btn = KeyboardButton(text=buttons.MOBILE_BANK_BTN_TEXT)
debit_card_btn = KeyboardButton(text=buttons.DEBIT_CARD_BTN_TEXT)
credit_card_btn = KeyboardButton(text=buttons.CREDIT_CARD_BTN_TEXT)
sim_card_btn = KeyboardButton(text=buttons.SIM_CARD_BTN_TEXT)
investments_btn = KeyboardButton(text=buttons.INVESTMENTS_BTN_TEXT)
junior_btn = KeyboardButton(text=buttons.JUNIOR_BTN_TEXT)
subscription_btn = KeyboardButton(text=buttons.SUBSCRIPTION_BTN_TEXT)
card_protection_btn = KeyboardButton(text=buttons.CARD_PROTECTION_BTN_TEXT)

# Main keyboard layout
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
main_keyboard.row(success_btn, postponed_btn, refused_btn)
main_keyboard.row(invite_friend_btn, transfer_abroad_btn, mobile_bank_btn)
main_keyboard.row(debit_card_btn, credit_card_btn, sim_card_btn)
main_keyboard.row(investments_btn, junior_btn, subscription_btn)
main_keyboard.row(card_protection_btn)
