import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from dotenv import load_dotenv
import os
from main import get_ongoing
from datetime import datetime


# инициализация .env файла
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot = Bot(token=os.getenv("TOKEN"), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await  message.answer('Жди, и скоро скину годноты')

    get_ongoing()
    date = datetime.today().strftime('%d-%m-%Y')

    await message.answer(f'Сегодня {date} вышли серии:')

    with open('data.json', encoding='utf-8') as file:
        data = json.load(file)
    for item in data:
        card = f'{hlink(item.get("head"), item.get("link"))}'
        await message.answer(card)

def main():
    executor.start_polling(dp)

if __name__ == "__main__":
    main()