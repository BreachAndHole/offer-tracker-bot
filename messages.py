from database import DailyResult


START_MESSAGE = '''
Привет, я - бот, помогающий вести тебе статистику встреч и продаж за день.

Команды:
/start или /help - вызвать основное меню и список команд
/new_day - начать новый рабочий день (обнулить статистику встреч и продаж)
/stat - сформировать сообщение со статистикой
'''


def form_stat_message(results: DailyResult) -> str:
    stat_message = f'''
Успешно: {results.success}
Перенос: {results.postponed}
Отмена: {results.canceled}

{results.invite_friend} пд
{results.transfer_abroad} переводы за рубеж
{results.mobile_bank} мб
{results.debit_card} дк
{results.credit_card} кк
{results.sim_card} сим
{results.investments} ти
{results.junior} джуниор
{results.subscription} подписка
'''
    return stat_message
