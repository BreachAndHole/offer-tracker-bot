from database import DailyResult


START_MESSAGE = '''
Привет, я - бот, помогающий вести тебе статистику встреч и продаж за день.

Команды:
/start или /help - вызвать основное меню и список команд
/new_day - начать новый рабочий день (обнулить статистику встреч и продаж)
/stat - сформировать сообщение со статистикой
'''


def form_stat_message(results: DailyResult) -> str:
    stat_message = ''
    if results.success:
        stat_message += f'Успешно: {results.success}\n'
    if results.postponed:
        stat_message += f'Перенос: {results.postponed}\n'
    if results.canceled:
        stat_message += f'Отмена: {results.canceled}\n'
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

    if not stat_message.strip():
        stat_message = 'В текущем дне не добавлено никаких результатов'

    return stat_message
