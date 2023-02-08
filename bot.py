import config
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message


bot = Bot(token=config.API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: Message):
    await message.delete()
    await message.answer('/start, /help - Вызвать меню и справку')


@dp.message_handler()
async def echo(message: Message):
    await message.delete()
    await message.answer(f'This is an echo to {message.text=}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
