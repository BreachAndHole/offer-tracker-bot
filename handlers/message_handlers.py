@dp.message_handler(commands=['start', 'help'])
async def start_command(message: Message):
    user = BotUser(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    is_new_user = database.add_user_to_database(user)
    if is_new_user:
        await bot.send_message(
            chat_id=config.ADMIN_ID,
            text=f'New user added: {user.first_name} {user.last_name}'
        )

    await message.delete()
    await message.answer(
        text=messages.START_MESSAGE,
        reply_markup=replyKeyboards.main_keyboard
    )


@dp.message_handler(commands=['stat', 'result'])
async def stat_command(message: Message):
    user = BotUser(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    daily_result = database.get_user_daily_result(user)
    reply_text = f'''
Успешно: {daily_result.success}
Перенос: {daily_result.postponed}
Отмена: {daily_result.canceled}

{daily_result.invite_friend} пд
{daily_result.transfer_abroad} переводы за рубеж
{daily_result.mobile_bank} мб
{daily_result.debit_card} дк
{daily_result.credit_card} кк
{daily_result.sim_card} сим
{daily_result.investments} ти
{daily_result.junior} джуниор
{daily_result.subscription} подписка
'''
    await message.answer(reply_text)


@dp.message_handler(Text(equals=main_buttons.success))
async def success_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.success_kb
    )