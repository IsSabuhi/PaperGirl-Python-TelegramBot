# -*- coding: cp1251 -*-
import json
import logging

from aiogram.utils.markdown import hlink, hbold

import config
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from parser import parser_discounts_game

# �������������� ����
bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
# ��������� ��� ����
dp = Dispatcher(bot)
# �������� �����������, ����� �� ���������� ������ ���������
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["���� �� ������� EG", "������� EG", "����������"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row()
    keyboard.add(*start_buttons)

    await message.answer('������ {0.first_name}'.format(message.from_user), reply_markup=keyboard)


@dp.message_handler(Text(equals="����������� ����� EG"))
async def get_discount_Game(message: types.Message):
    await message.answer("���������� ���������...")

    parser_discounts_game()

    with open("new_json.json") as file:
        data = json.load(file)

    for item in data:
        card = f"{hlink(item.get('url'), item.get('url'))}\n" \
               f"{hbold('���������: ')} {item.get('title')}\n" \
               f"{hbold('��������: ')} {item.get('description')}\n" \
               f"{hbold('����: ')} {item.get('price')}\n" \
               f"{hbold('���� �� �������: ')} {item.get('discountPrice')}\n" \
               f"{hbold('���� ������ �����: ')} {item.get('startDate')}\n" \
               f"{hbold('���� ����� �����: ')} {item.get('endDate')}\n" \

        await message.answer(card)


@dp.message_handler(Text(equals="������� EG"))
async def ShopEG(message: types.Message):
    await bot.send_message(message.from_user.id, "���� ������ �� ������� Epic games " + str('epicgames.com/'))


@dp.message_handler(Text(equals="����������"))
async def Info(message: types.Message):
    # linkDB = hlink('PaperGirl Aya', '')

    cardInfo = f"{hbold('������������: ')} : ��������� ������, ����� ���������, �������� �������\n" \
               f"{hbold('��� ����: ')} : ����� ����� ������ �� ���� ���� ���� ��������� �� ������ :)\n" \
               f"{hbold('������� ���: ')} : {hlink('PaperGirl Aya', '')}" \

    # await message.answer(cardInfo)

    await bot.send_message(message.from_user.id, cardInfo)


if __name__ == '__main__':
    executor.start_polling(dp)