from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


cancel_btn = InlineKeyboardButton(text='Отмена', callback_data='cancel_btn')

# Success
success_add_btn = InlineKeyboardButton(text='+1', callback_data='success_add_btn')
success_remove_btn = InlineKeyboardButton(text='-1', callback_data='success_remove_btn')
success_kb = InlineKeyboardMarkup(row_width=2)
success_kb.row(success_add_btn, success_remove_btn)
success_kb.row(cancel_btn)

# Postponed
postponed_add_btn = InlineKeyboardButton(text='+1', callback_data='postponed_add_btn')
postponed_remove_btn = InlineKeyboardButton(text='-1', callback_data='postponed_remove_btn')
postponed_kb = InlineKeyboardMarkup(row_width=2)
postponed_kb.row(postponed_add_btn, postponed_remove_btn)
postponed_kb.row(cancel_btn)

# Canceled
canceled_add_btn = InlineKeyboardButton(text='+1', callback_data='canceled_add_btn')
canceled_remove_btn = InlineKeyboardButton(text='-1', callback_data='canceled_remove_btn')
canceled_kb = InlineKeyboardMarkup(row_width=2)
canceled_kb.row(canceled_add_btn, canceled_remove_btn)
canceled_kb.row(cancel_btn)

# Invite friend
invite_add_btn = InlineKeyboardButton(text='+1', callback_data='invite_add_btn')
invite_remove_btn = InlineKeyboardButton(text='-1', callback_data='invite_remove_btn')
invite_kb = InlineKeyboardMarkup(row_width=2)
invite_kb.row(invite_add_btn, invite_remove_btn)
invite_kb.row(cancel_btn)


# Transfer abroad
transfer_add_btn = InlineKeyboardButton(text='+1', callback_data='transfer_add_btn')
transfer_remove_btn = InlineKeyboardButton(text='-1', callback_data='transfer_remove_btn')
transfer_kb = InlineKeyboardMarkup(row_width=2)
transfer_kb.row(transfer_add_btn, transfer_remove_btn)
transfer_kb.row(cancel_btn)

# Mobile bank
mobile_add_btn = InlineKeyboardButton(text='+1', callback_data='mobile_add_btn')
mobile_remove_btn = InlineKeyboardButton(text='-1', callback_data='mobile_remove_btn')
mobile_kb = InlineKeyboardMarkup(row_width=2)
mobile_kb.row(mobile_add_btn, mobile_remove_btn)
mobile_kb.row(cancel_btn)

# Debit card
debit_add_btn = InlineKeyboardButton(text='+1', callback_data='debit_add_btn')
debit_remove_btn = InlineKeyboardButton(text='-1', callback_data='debit_remove_btn')
debit_kb = InlineKeyboardMarkup(row_width=2)
debit_kb.row(debit_add_btn, debit_remove_btn)
debit_kb.row(cancel_btn)

# Credit card
credit_add_btn = InlineKeyboardButton(text='+1', callback_data='credit_add_btn')
credit_remove_btn = InlineKeyboardButton(text='-1', callback_data='credit_remove_btn')
credit_kb = InlineKeyboardMarkup(row_width=2)
credit_kb.row(credit_add_btn, credit_remove_btn)
credit_kb.row(cancel_btn)

# Sim card
sim_add_btn = InlineKeyboardButton(text='+1', callback_data='sim_add_btn')
sim_remove_btn = InlineKeyboardButton(text='-1', callback_data='sim_remove_btn')
sim_kb = InlineKeyboardMarkup(row_width=2)
sim_kb.row(sim_add_btn, sim_remove_btn)
sim_kb.row(cancel_btn)

# Investments
investments_add_btn = InlineKeyboardButton(text='+1', callback_data='investments_add_btn')
investments_remove_btn = InlineKeyboardButton(text='-1', callback_data='investments_remove_btn')
investments_kb = InlineKeyboardMarkup(row_width=2)
investments_kb.row(investments_add_btn, investments_remove_btn)
investments_kb.row(cancel_btn)

# Junior
junior_add_btn = InlineKeyboardButton(text='+1', callback_data='junior_add_btn')
junior_remove_btn = InlineKeyboardButton(text='-1', callback_data='junior_remove_btn')
junior_kb = InlineKeyboardMarkup(row_width=2)
junior_kb.row(junior_add_btn, junior_remove_btn)
junior_kb.row(cancel_btn)

# Subscription
subscription_add_btn = InlineKeyboardButton(text='+1', callback_data='subscription_add_btn')
subscription_remove_btn = InlineKeyboardButton(text='-1', callback_data='subscription_remove_btn')
subscription_kb = InlineKeyboardMarkup(row_width=2)
subscription_kb.row(subscription_add_btn, subscription_remove_btn)
subscription_kb.row(cancel_btn)