import json
import logging

from aiogram.utils.markdown import hlink, hbold

import config
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from parser import parser_file

# инициализируем бота
bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Бесплатные игры EG", "Игры со скидкой EG", "Магазин EG", "Информация"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row()
    keyboard.add(*start_buttons)

    await message.answer('Привет {0.first_name}'.format(message.from_user), reply_markup=keyboard)


@dp.message_handler(Text(equals="Бесплатные игры EG"))
async def get_freeGame(message: types.Message):
    await message.answer("Пожалуйста подождите...")

    parser_file()

    with open("new_json.json") as file:
        data = json.load(file)

    for item in data:
        card = f"{hlink(item.get('url'), item.get('url'))}\n" \
               f"{hbold('Заголовок: ')} {item.get('title')}\n" \
               f"{hbold('Описание: ')} {item.get('description')}\n" \
               f"{hbold('Цена: ')} {item.get('price')}\n" \
               f"{hbold('Цена со скидкой: ')} {item.get('discountPrice')}\n" \

        await message.answer(card)


@dp.message_handler(Text(equals="Магазин EG"))
async def ShopEG(message: types.Message):
    await bot.send_message(message.from_user.id, "Ваша ссылка на магазин Epic games " + str('epicgames.com/'))


if __name__ == '__main__':
    executor.start_polling(dp)
