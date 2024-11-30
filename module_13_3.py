import aiogram as ai
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7514207461:AAGu7ivIl_q3aDoo9-HQeRZEklGmNYjblD8'
bot = ai.Bot(token=api)
dp = ai.Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print('Urban message')


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

"""Чтобы достать из отправленного боту сообщения текст нужно брать параметр текст
message.text"""
@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    ai.executor.start_polling(dp, skip_updates=True)
