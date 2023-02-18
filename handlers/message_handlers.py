from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from config.basic import ADMIN_ID
from config import messages, buttons
from keyboards import reply, inline
from services import message_services, database_services
from bot import bot


async def start_command(message: Message):
    # Adding user to database if he is new and messaging about it to admin
    if database_services.add_user_to_database(message.from_user.id):
        await bot.send_message(
            chat_id=ADMIN_ID,
            text=f'New user added: {message.from_user.first_name} {message.from_user.last_name}'
        )

    await message.answer(
        text=messages.START_MESSAGE,
        reply_markup=reply.main_keyboard
    )


async def stat_command(message: Message):
    daily_result = database_services.get_user_result(message.from_user.id)
    reply_text = message_services.form_result_message(daily_result)
    await message.answer(reply_text)


async def success_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.success_kb
    )


async def postponed_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.postponed_kb
    )


async def refused_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.refused_kb
    )


async def invite_friend_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.invite_kb
    )


async def transfer_abroad_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.transfer_kb
    )


async def mobile_bank_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.mobile_kb
    )


async def debit_card_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.debit_kb
    )


async def credit_card_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.credit_kb
    )


async def sim_card_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.sim_kb
    )


async def investments_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.investments_kb
    )


async def junior_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.junior_kb
    )


async def subscription_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.subscription_kb
    )


async def card_protection_menu(message: Message):
    await message.delete()
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=inline.card_protection_kb
    )


async def reset_command(message: Message):
    await message.delete()
    await message.answer(
        'Вы действительно хотите сбросить текущие результаты встреч и офферов?',
        reply_markup=inline.reset_kb
    )


async def feedback_command(message: Message):
    is_text_exists = message.text.replace("/feedback", "") != ''
    if not is_text_exists:
        await message.answer(messages.FEEDBACK_NOT_SENT)
        return

    feedback = message_services.form_feedback_message(message)
    await message.answer(messages.FEEDBACK_SENT)
    await bot.send_message(chat_id=ADMIN_ID, text=feedback)


def setup(dp: Dispatcher):
    # Commands
    dp.register_message_handler(start_command, commands=['start', 'help', 'старт'])
    dp.register_message_handler(stat_command, commands=['result', 'результат'])
    dp.register_message_handler(reset_command, commands=['reset', 'сбросить'])
    dp.register_message_handler(feedback_command, commands=['feedback'])

    # Inline handlers
    dp.register_message_handler(success_menu, Text(equals=buttons.SUCCESS_BTN_TEXT))
    dp.register_message_handler(postponed_menu, Text(equals=buttons.POSTPONED_BTN_TEXT))
    dp.register_message_handler(refused_menu, Text(equals=buttons.REFUSED_BTN_TEXT))
    dp.register_message_handler(invite_friend_menu, Text(equals=buttons.INVITE_FRIEND_BTN_TEXT))
    dp.register_message_handler(transfer_abroad_menu, Text(equals=buttons.TRANSFER_ABROAD_BTN_TEXT))
    dp.register_message_handler(mobile_bank_menu, Text(equals=buttons.MOBILE_BANK_BTN_TEXT))
    dp.register_message_handler(debit_card_menu, Text(equals=buttons.DEBIT_CARD_BTN_TEXT))
    dp.register_message_handler(credit_card_menu, Text(equals=buttons.CREDIT_CARD_BTN_TEXT))
    dp.register_message_handler(sim_card_menu, Text(equals=buttons.SIM_CARD_BTN_TEXT))
    dp.register_message_handler(investments_menu, Text(equals=buttons.INVESTMENTS_BTN_TEXT))
    dp.register_message_handler(junior_menu, Text(equals=buttons.JUNIOR_BTN_TEXT))
    dp.register_message_handler(subscription_menu, Text(equals=buttons.SUBSCRIPTION_BTN_TEXT))
    dp.register_message_handler(card_protection_menu, Text(equals=buttons.CARD_PROTECTION_BTN_TEXT))
