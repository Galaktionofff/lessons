import aiogram as ai
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = ai.Bot(token=api)
dp = ai.Dispatcher(bot, storage=MemoryStorage())


class User_state(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст')
    await User_state.age.set()


@dp.message_handler(state=User_state.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await User_state.growth.set()


@dp.message_handler(state=User_state.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await User_state.weight.set()


@dp.message_handler(state=User_state.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    await message.answer(f'Ваша норма калорий {10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"])}')
    await state.finish()


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
