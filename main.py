import logging
import config
import json
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import buttons as btn



# инициализируем бота
bot = Bot(token=config.API_TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup=btn.mainMenu)

@dp.message_handler()
async def bot_message():
    async def buttons_link(message: types.Message):
        if message.text == "Главное меню":
            await bot.send_message(message.from_user.id, "Главное меню", reply_markup=btn.mainMenu)
        elif message.text == "Информация":
            await bot.send_message(message.from_user.id, reply_markup=btn.btnInfo)
        elif message.text == "Epic Games":
            await bot.send_message(message.from_user.id, "Ваша ссылка на магазин Epic games " + str('epicgames.com/'))
        elif message.text == "Steam":
            await bot.send_message(message.from_user.id, "Ваша ссылка на магазин Steam " + str('store.steampowered.com/'))
        elif message.text == "Назад":
            await bot.send_message(message.from_user.id, "Назад", reply_markup=btn.mainMenu)
        elif message.text == "Магазины":
            await bot.send_message(message.from_user.id, "Магазины", reply_markup=btn.MenuShop)
        else:
            message.reply("Неизвестная команда")



# @dp.message_handler(commands='start')
# async def process_start_command(message: types.Message):
#     start_button = ["Start", "Stop", 'Help']
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(*start_button)
#
#     await message.answer("Привет!", reply_markup=keyboard)

# @dp.message_handler(Text(equals="Start"))
# async def get_discount_game(message: types.Message):
#     await message.answer("Пожалуйса подождите...")
#
#     with open("data.json") as file:
#         data = json.load(file)
#
#     for item in data:
#         card = f"{hlink(item.get('Ссылка'), item.get('url'))}\n" \
#                f"{hlink(item.get('title'), item.get('link'))}\n" \
#                f"{hbold('Описание: ')} {item.get('description')}\n"
#         await message.answer(card)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
