from typing import NamedTuple


class KeyboardButtons(NamedTuple):
    success: str
    postponed: str
    canceled: str
    invite_friend: str
    transfer_abroad: str
    mobile_bank: str
    debit_card: str
    credit_card: str
    sim_card: str
    investments: str
    junior: str
    subscription: str


class CallbackText(NamedTuple):
    add: str
    remove: str


class InlineButtons(NamedTuple):
    success: CallbackText
    postponed: CallbackText
    canceled: CallbackText
    invite_friend: CallbackText
    transfer_abroad: CallbackText
    mobile_bank: CallbackText
    debit_card: CallbackText
    credit_card: CallbackText
    sim_card: CallbackText
    investments: CallbackText
    junior: CallbackText
    subscription: CallbackText
    cancel: str


main_kb_buttons = KeyboardButtons(
    success='Успешные',
    postponed='Переносы',
    canceled='Отказы',
    invite_friend='Приведи друга',
    transfer_abroad='Перевод за рубеж',
    mobile_bank='Мобильный банк',
    debit_card='Дебетовая карта',
    credit_card='Кредитная карта',
    sim_card='Тинькофф Мобайл',
    investments='Инвестиции',
    junior='Джуниор',
    subscription='Подписка PRO',
)

success_callback = CallbackText('success_add_btn', 'success_remove_btn')
postponed_callback = CallbackText('postponed_add_btn', 'postponed_remove_btn')
canceled_callback = CallbackText('canceled_add_btn', 'canceled_remove_btn')
invite_callback = CallbackText('invite_add_btn', 'invite_remove_btn')
transfer_callback = CallbackText('transfer_add_btn', 'transfer_remove_btn')
mobile_bank_callback = CallbackText('mobile_add_btn', 'mobile_remove_btn')
debit_card_callback = CallbackText('debit_add_btn', 'debit_remove_btn')
credit_card_callback = CallbackText('credit_add_btn', 'credit_remove_btn')
sim_card_callback = CallbackText('sim_add_btn', 'sim_remove_btn')
investments_callback = CallbackText('investments_add_btn', 'investments_remove_btn')
junior_callback = CallbackText('junior_add_btn', 'junior_remove_btn')
subscription_callback = CallbackText('subscription_add_btn', 'subscription_remove_btn')

inline_buttons = InlineButtons(
    success=success_callback,
    postponed=postponed_callback,
    canceled=canceled_callback,
    invite_friend=invite_callback,
    transfer_abroad=transfer_callback,
    mobile_bank=mobile_bank_callback,
    debit_card=debit_card_callback,
    credit_card=credit_card_callback,
    sim_card=sim_card_callback,
    investments=investments_callback,
    junior=junior_callback,
    subscription=subscription_callback,
    cancel='cancel_btn'
)
