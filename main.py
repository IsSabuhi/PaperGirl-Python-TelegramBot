# -*- coding: cp1251 -*-
import json
import logging

from aiogram.utils.markdown import hlink, hbold

import config
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from parser import parser_discounts_game

# инициализируем бота
bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Игры со скидкой EG", "Магазин EG", "Информация"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row()
    keyboard.add(*start_buttons)

    await message.answer('Привет {0.first_name}'.format(message.from_user), reply_markup=keyboard)


@dp.message_handler(Text(equals="Действующие акции EG"))
async def get_discount_Game(message: types.Message):
    await message.answer("Пожалуйста подождите...")

    parser_discounts_game()

    with open("new_json.json") as file:
        data = json.load(file)

    for item in data:
        card = f"{hlink(item.get('url'), item.get('url'))}\n" \
               f"{hbold('Заголовок: ')} {item.get('title')}\n" \
               f"{hbold('Описание: ')} {item.get('description')}\n" \
               f"{hbold('Цена: ')} {item.get('price')}\n" \
               f"{hbold('Цена со скидкой: ')} {item.get('discountPrice')}\n" \
               f"{hbold('Дата начала акции: ')} {item.get('startDate')}\n" \
               f"{hbold('Дата конца акции: ')} {item.get('endDate')}\n" \

        await message.answer(card)


@dp.message_handler(Text(equals="Магазин EG"))
async def ShopEG(message: types.Message):
    await bot.send_message(message.from_user.id, "Ваша ссылка на магазин Epic games " + str('epicgames.com/'))


@dp.message_handler(Text(equals="Информация"))
async def Info(message: types.Message):
    # linkDB = hlink('PaperGirl Aya', '')

    cardInfo = f"{hbold('Разработчики: ')} : Исрафилов Сабухи, Антон Силинский, Паргачёв Алексей\n" \
               f"{hbold('Наш сайт: ')} : Здесь будет ссылка на сайт если Тоха развернет на сервак :)\n" \
               f"{hbold('Дискорд бот: ')} : {hlink('PaperGirl Aya', '')}" \

    # await message.answer(cardInfo)

    await bot.send_message(message.from_user.id, cardInfo)


if __name__ == '__main__':
    executor.start_polling(dp)