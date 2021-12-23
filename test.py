# -*- coding: cp1251 -*-
import asyncio
import json
import logging
from datetime import datetime

import schedule, time
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

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


async def setup_bot_commands(dp):
    bot_commands = [
        types.BotCommand(command="start", description="Запустить бота"),
        types.BotCommand(command="promo", description="Список действующих и ближайших акций"),
        types.BotCommand(command="shop", description="Ссылка на магазин Epic Games"),
        types.BotCommand(command="info", description="Информация"),
        types.BotCommand(command="help", description="Отображает список всех доступных команд")
    ]
    await bot.set_my_commands(bot_commands)


@dp.message_handler(commands="help")
async def help_info(message: types.Message):
    await message.answer(
        text='''
        Мои команды:
        /start - Запускает бота
        /promo - Список действующих и ближайших акций
        /shop - Ссылка на магазин Epic Games
        /info - Информация
        /help - Отображает список всех доступных команд
        '''
    )


@dp.message_handler(commands="start")
async def start_bot(message: types.Message):
    await message.answer('Привет {0.first_name} !\nЯ - PaperGirl Aya!\nЯ буду отправлять тебе уведомление о новый акциях в Epic Games :)'.format(message.from_user))

@dp.message_handler(commands=["promo"])
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


@dp.message_handler(commands=["shop"])
async def ShopEG(message: types.Message):
    await bot.send_message(message.from_user.id, "Ваша ссылка на магазин Epic games " + str('epicgames.com/'))


@dp.message_handler(commands=["info"])
async def Info(message: types.Message):
    cardInfo = f"{hbold('Разработчики: ')} : Исрафилов Сабухи, Силинский Антон, Паргачёв Алексей\n" \
               f"{hbold('Наш сайт: ')} : Здесь будет ссылка на сайт если Тоха развернет на сервак :)\n" \
               f"{hbold('Дискорд бот: ')} : {hlink('PaperGirl Aya', '')}" \

    await bot.send_message(message.from_user.id, cardInfo)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=setup_bot_commands)

