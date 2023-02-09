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


main_kb_buttons = KeyboardButtons(
    success='Успешные',
    postponed='Переносы',
    canceled='Отказы',
    invite_friend='Пригласи друга',
    transfer_abroad='Перевод за рубеж',
    mobile_bank='Мобильный банк',
    debit_card='Дебетовая карта',
    credit_card='Кредитная карта',
    sim_card='Тинькофф Мобайл',
    investments='Инвестиции',
    junior='Джуниор',
    subscription='Подписка PRO',
)
