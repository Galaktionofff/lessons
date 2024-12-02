import aiogram as ai
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = ai.Bot(token=api)
dp = ai.Dispatcher(bot, storage=MemoryStorage())

"""Создание клавиатуры кнопок"""
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Информация')
button1 = KeyboardButton(text='Рассчитать')
keyboard.add(button)
keyboard.add(button1)

"""Создание инлайновых(внутри сообщений) кнопок"""
kb_il = InlineKeyboardMarkup()
Inline_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
Inline_button1 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_il.add(Inline_button)
kb_il.add(Inline_button1)


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет!  Я бот помогающий твоему здоровью.', reply_markup=keyboard)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb_il)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 х рост (см) - 5 х возраст (г) - 161')
    await call.answer()


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer("Меня сделал Никитос")


class User_state(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await call.answer()
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


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    ai.executor.start_polling(dp, skip_updates=True)
