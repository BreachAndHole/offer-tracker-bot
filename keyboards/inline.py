from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import callbacks


cancel_btn = InlineKeyboardButton(text='Отмена', callback_data=callbacks.CANCEL)

# Success
success_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.SUCCESS_ADD)
success_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.SUCCESS_REMOVE)
success_kb = InlineKeyboardMarkup(row_width=2)
success_kb.row(success_add_btn, success_remove_btn)
success_kb.row(cancel_btn)

# Postponed
postponed_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.POSTPONED_ADD)
postponed_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.POSTPONED_REMOVE)
postponed_kb = InlineKeyboardMarkup(row_width=2)
postponed_kb.row(postponed_add_btn, postponed_remove_btn)
postponed_kb.row(cancel_btn)

# Refused
refused_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.REFUSED_ADD)
refused_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.REFUSED_REMOVE)
refused_kb = InlineKeyboardMarkup(row_width=2)
refused_kb.row(refused_add_btn, refused_remove_btn)
refused_kb.row(cancel_btn)

# Invite friend
invite_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.INVITE_FRIEND_ADD)
invite_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.INVITE_FRIEND_REMOVE)
invite_kb = InlineKeyboardMarkup(row_width=2)
invite_kb.row(invite_add_btn, invite_remove_btn)
invite_kb.row(cancel_btn)

# Transfer abroad
transfer_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.TRANSFER_ABROAD_ADD)
transfer_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.TRANSFER_ABROAD_REMOVE)
transfer_kb = InlineKeyboardMarkup(row_width=2)
transfer_kb.row(transfer_add_btn, transfer_remove_btn)
transfer_kb.row(cancel_btn)

# Mobile bank
mobile_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.MOBILE_BANK_ADD)
mobile_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.MOBILE_BANK_REMOVE)
mobile_kb = InlineKeyboardMarkup(row_width=2)
mobile_kb.row(mobile_add_btn, mobile_remove_btn)
mobile_kb.row(cancel_btn)

# Debit card
debit_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.DEBIT_CARD_ADD)
debit_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.DEBIT_CARD_REMOVE)
debit_kb = InlineKeyboardMarkup(row_width=2)
debit_kb.row(debit_add_btn, debit_remove_btn)
debit_kb.row(cancel_btn)

# Credit card
credit_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.CREDIT_CARD_ADD)
credit_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.CREDIT_CARD_REMOVE)
credit_kb = InlineKeyboardMarkup(row_width=2)
credit_kb.row(credit_add_btn, credit_remove_btn)
credit_kb.row(cancel_btn)

# Sim card
sim_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.SIM_CARD_ADD)
sim_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.SIM_CARD_REMOVE)
sim_kb = InlineKeyboardMarkup(row_width=2)
sim_kb.row(sim_add_btn, sim_remove_btn)
sim_kb.row(cancel_btn)

# Investments
investments_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.INVESTMENTS_ADD)
investments_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.INVESTMENTS_REMOVE)
investments_kb = InlineKeyboardMarkup(row_width=2)
investments_kb.row(investments_add_btn, investments_remove_btn)
investments_kb.row(cancel_btn)

# Junior
junior_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.JUNIOR_ADD)
junior_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.JUNIOR_REMOVE)
junior_kb = InlineKeyboardMarkup(row_width=2)
junior_kb.row(junior_add_btn, junior_remove_btn)
junior_kb.row(cancel_btn)

# Subscription
subscription_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.SUBSCRIPTION_ADD)
subscription_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.SUBSCRIPTION_REMOVE)
subscription_kb = InlineKeyboardMarkup(row_width=2)
subscription_kb.row(subscription_add_btn, subscription_remove_btn)
subscription_kb.row(cancel_btn)

# Card protection
card_protection_add_btn = InlineKeyboardButton(text='+1', callback_data=callbacks.CARD_PROTECTION_ADD)
card_protection_remove_btn = InlineKeyboardButton(text='-1', callback_data=callbacks.CARD_PROTECTION_REMOVE)
card_protection_kb = InlineKeyboardMarkup(row_width=2)
card_protection_kb.row(card_protection_add_btn, card_protection_remove_btn)
card_protection_kb.row(cancel_btn)
