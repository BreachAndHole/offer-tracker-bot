from aiogram.types import Message
from structures import DailyResult


def form_result_message(results: DailyResult) -> str:
    stat_message = ''
    if results.success:
        stat_message += f'Успешно: {results.success}\n'
    if results.postponed:
        stat_message += f'Перенос: {results.postponed}\n'
    if results.refused:
        stat_message += f'Отмена: {results.refused}\n'
    stat_message += '\n'
    if results.invite_friend:
        stat_message += f'{results.invite_friend} пд\n'
    if results.transfer_abroad:
        stat_message += f'{results.transfer_abroad} перевод за рубеж\n'
    if results.mobile_bank:
        stat_message += f'{results.mobile_bank} мб\n'
    if results.debit_card:
        stat_message += f'{results.debit_card} дк\n'
    if results.credit_card:
        stat_message += f'{results.credit_card} кк\n'
    if results.sim_card:
        stat_message += f'{results.sim_card} сим\n'
    if results.investments:
        stat_message += f'{results.investments} ти\n'
    if results.junior:
        stat_message += f'{results.junior} джуниор\n'
    if results.subscription:
        stat_message += f'{results.subscription} подписка\n'
    if results.card_protection:
        stat_message += f'{results.card_protection} защита карты\n'

    if not stat_message.strip():
        stat_message = 'В текущем дне не добавлено никаких результатов'

    return stat_message


def form_feedback_message(message: Message) -> str:
    feedback = f'Пришел новый #feedback\n' \
               f'Пользователь: {message.from_user.first_name} {message.from_user.last_name}\n' \
               f'ID: {message.from_user.id}\n\n' \
               f'Текст: {message.text.replace("/feedback", "")}'
    return feedback
