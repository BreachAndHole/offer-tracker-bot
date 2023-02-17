from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.buttons_config import inline_buttons


cancel_btn = InlineKeyboardButton(text='Отмена', callback_data=inline_buttons.cancel)

# Success
success_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.success.add)
success_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.success.remove)
success_kb = InlineKeyboardMarkup(row_width=2)
success_kb.row(success_add_btn, success_remove_btn)
success_kb.row(cancel_btn)

# Postponed
postponed_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.postponed.add)
postponed_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.postponed.remove)
postponed_kb = InlineKeyboardMarkup(row_width=2)
postponed_kb.row(postponed_add_btn, postponed_remove_btn)
postponed_kb.row(cancel_btn)

# Refused
refused_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.refused.add)
refused_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.refused.remove)
refused_kb = InlineKeyboardMarkup(row_width=2)
refused_kb.row(refused_add_btn, refused_remove_btn)
refused_kb.row(cancel_btn)

# Invite friend
invite_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.invite_friend.add)
invite_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.invite_friend.remove)
invite_kb = InlineKeyboardMarkup(row_width=2)
invite_kb.row(invite_add_btn, invite_remove_btn)
invite_kb.row(cancel_btn)

# Transfer abroad
transfer_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.transfer_abroad.add)
transfer_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.transfer_abroad.remove)
transfer_kb = InlineKeyboardMarkup(row_width=2)
transfer_kb.row(transfer_add_btn, transfer_remove_btn)
transfer_kb.row(cancel_btn)

# Mobile bank
mobile_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.mobile_bank.add)
mobile_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.mobile_bank.remove)
mobile_kb = InlineKeyboardMarkup(row_width=2)
mobile_kb.row(mobile_add_btn, mobile_remove_btn)
mobile_kb.row(cancel_btn)

# Debit card
debit_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.debit_card.add)
debit_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.debit_card.remove)
debit_kb = InlineKeyboardMarkup(row_width=2)
debit_kb.row(debit_add_btn, debit_remove_btn)
debit_kb.row(cancel_btn)

# Credit card
credit_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.credit_card.add)
credit_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.credit_card.remove)
credit_kb = InlineKeyboardMarkup(row_width=2)
credit_kb.row(credit_add_btn, credit_remove_btn)
credit_kb.row(cancel_btn)

# Sim card
sim_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.sim_card.add)
sim_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.sim_card.remove)
sim_kb = InlineKeyboardMarkup(row_width=2)
sim_kb.row(sim_add_btn, sim_remove_btn)
sim_kb.row(cancel_btn)

# Investments
investments_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.investments.add)
investments_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.investments.remove)
investments_kb = InlineKeyboardMarkup(row_width=2)
investments_kb.row(investments_add_btn, investments_remove_btn)
investments_kb.row(cancel_btn)

# Junior
junior_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.junior.add)
junior_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.junior.remove)
junior_kb = InlineKeyboardMarkup(row_width=2)
junior_kb.row(junior_add_btn, junior_remove_btn)
junior_kb.row(cancel_btn)

# Subscription
subscription_add_btn = InlineKeyboardButton(text='+1', callback_data=inline_buttons.subscription.add)
subscription_remove_btn = InlineKeyboardButton(text='-1', callback_data=inline_buttons.subscription.remove)
subscription_kb = InlineKeyboardMarkup(row_width=2)
subscription_kb.row(subscription_add_btn, subscription_remove_btn)
subscription_kb.row(cancel_btn)
