from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from keyboards.buttons_config import main_kb_buttons


# Results keyboard buttons
# Meeting results
success_btn = KeyboardButton(text=main_kb_buttons.success)
postponed_btn = KeyboardButton(text=main_kb_buttons.postponed)
refused_btn = KeyboardButton(text=main_kb_buttons.refused)
# Offers
invite_friend_btn = KeyboardButton(text=main_kb_buttons.invite_friend)
transfer_abroad_btn = KeyboardButton(text=main_kb_buttons.transfer_abroad)
mobile_bank_btn = KeyboardButton(text=main_kb_buttons.mobile_bank)
debit_card_btn = KeyboardButton(text=main_kb_buttons.debit_card)
credit_card_btn = KeyboardButton(text=main_kb_buttons.credit_card)
sim_card_btn = KeyboardButton(text=main_kb_buttons.sim_card)
investments_btn = KeyboardButton(text=main_kb_buttons.investments)
junior_btn = KeyboardButton(text=main_kb_buttons.junior)
subscription_btn = KeyboardButton(text=main_kb_buttons.subscription)
card_protection_btn = KeyboardButton(text=main_kb_buttons.card_protection)

# Main keyboard layout
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
main_keyboard.row(success_btn, postponed_btn, refused_btn)
main_keyboard.row(invite_friend_btn, transfer_abroad_btn, mobile_bank_btn)
main_keyboard.row(debit_card_btn, credit_card_btn, sim_card_btn)
main_keyboard.row(investments_btn, junior_btn, subscription_btn)
main_keyboard.row(card_protection_btn)
