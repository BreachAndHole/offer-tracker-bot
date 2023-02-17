from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

import database
import messages
from config import ADMIN_ID
from keyboards.buttons_config import main_kb_buttons
from keyboards import replyKeyboards, inlineKeyboards
from bot import bot


async def start_command(message: Message):
    user = database.BotUser(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )

    # Adding user to database if he is new and messaging about it to admin
    if database.add_user_to_database(user):
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=f'New user added: {user.first_name} {user.last_name}'
        )

    # Delete message and open main keyboard
    await message.answer(
        text=messages.START_MESSAGE,
        reply_markup=replyKeyboards.main_keyboard
    )


async def stat_command(message: Message):
    user = database.BotUser(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    daily_result = database.get_user_daily_result(user)
    reply_text = messages.form_stat_message(daily_result)
    await message.answer(reply_text)


async def success_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.success_kb
    )


async def postponed_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.postponed_kb
    )


async def refused_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.refused_kb
    )


async def invite_friend_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.invite_kb
    )


async def transfer_abroad_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.transfer_kb
    )


async def mobile_bank_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.mobile_kb
    )


async def debit_card_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.debit_kb
    )


async def credit_card_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.credit_kb
    )


async def sim_card_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.sim_kb
    )


async def investments_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.investments_kb
    )


async def junior_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.junior_kb
    )


async def subscription_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.subscription_kb
    )


async def card_protection_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inlineKeyboards.card_protection_kb
    )


async def new_day_command(message: Message):
    database.reset_user_result(message.from_user.id)
    await message.delete()
    await message.answer('Результаты сброшены. Удачного дня!')


def setup(dp: Dispatcher):
    # Commands
    dp.register_message_handler(start_command, commands=['start', 'help', 'старт'])
    dp.register_message_handler(stat_command, commands=['result', 'результат'])
    dp.register_message_handler(new_day_command, commands=['reset', 'сбросить'])

    # Inline handlers
    dp.register_message_handler(success_menu, Text(equals=main_kb_buttons.success))
    dp.register_message_handler(postponed_menu, Text(equals=main_kb_buttons.postponed))
    dp.register_message_handler(refused_menu, Text(equals=main_kb_buttons.refused))
    dp.register_message_handler(invite_friend_menu, Text(equals=main_kb_buttons.invite_friend))
    dp.register_message_handler(transfer_abroad_menu, Text(equals=main_kb_buttons.transfer_abroad))
    dp.register_message_handler(mobile_bank_menu, Text(equals=main_kb_buttons.mobile_bank))
    dp.register_message_handler(debit_card_menu, Text(equals=main_kb_buttons.debit_card))
    dp.register_message_handler(credit_card_menu, Text(equals=main_kb_buttons.credit_card))
    dp.register_message_handler(sim_card_menu, Text(equals=main_kb_buttons.sim_card))
    dp.register_message_handler(investments_menu, Text(equals=main_kb_buttons.investments))
    dp.register_message_handler(junior_menu, Text(equals=main_kb_buttons.junior))
    dp.register_message_handler(subscription_menu, Text(equals=main_kb_buttons.subscription))
    dp.register_message_handler(card_protection_menu, Text(equals=main_kb_buttons.card_protection))
