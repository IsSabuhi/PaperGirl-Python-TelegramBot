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

# �������������� ����
bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
# ��������� ��� ����
dp = Dispatcher(bot)
# �������� �����������, ����� �� ���������� ������ ���������
logging.basicConfig(level=logging.INFO)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


async def setup_bot_commands(dp):
    bot_commands = [
        types.BotCommand(command="start", description="��������� ����"),
        types.BotCommand(command="promo", description="������ ����������� � ��������� �����"),
        types.BotCommand(command="shop", description="������ �� ������� Epic Games"),
        types.BotCommand(command="info", description="����������"),
        types.BotCommand(command="help", description="���������� ������ ���� ��������� ������")
    ]
    await bot.set_my_commands(bot_commands)


@dp.message_handler(commands="help")
async def help_info(message: types.Message):
    await message.answer(
        text='''
        ��� �������:
        /start - ��������� ����
        /promo - ������ ����������� � ��������� �����
        /shop - ������ �� ������� Epic Games
        /info - ����������
        /help - ���������� ������ ���� ��������� ������
        '''
    )


@dp.message_handler(commands="start")
async def start_bot(message: types.Message):
    await message.answer('������ {0.first_name} !\n� - PaperGirl Aya!\n� ���� ���������� ���� ����������� � ����� ������ � Epic Games :)'.format(message.from_user))

@dp.message_handler(commands=["promo"])
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


@dp.message_handler(commands=["shop"])
async def ShopEG(message: types.Message):
    await bot.send_message(message.from_user.id, "���� ������ �� ������� Epic games " + str('epicgames.com/'))


@dp.message_handler(commands=["info"])
async def Info(message: types.Message):
    cardInfo = f"{hbold('������������: ')} : ��������� ������, ��������� �����, �������� �������\n" \
               f"{hbold('��� ����: ')} : ����� ����� ������ �� ���� ���� ���� ��������� �� ������ :)\n" \
               f"{hbold('������� ���: ')} : {hlink('PaperGirl Aya', '')}" \

    await bot.send_message(message.from_user.id, cardInfo)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=setup_bot_commands)

