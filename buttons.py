from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton("Главное меню")
btnInfo = KeyboardButton("Информация")
# infoMain = ReplyKeyboardMarkup(resize_keyboard=True).add(btnShop, btnBot, btnWS, btnDev)

# Main menu
btnShop = KeyboardButton("Магазины")
btnBot = KeyboardButton("Наши боты")
btnWS = KeyboardButton("Наш сайт")
btnDev = KeyboardButton("Разработчик")
back = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo)

# Other Menu
btnBack = KeyboardButton("Назад")
btnEP = KeyboardButton("Epic Games")
btnST = KeyboardButton("Steam")
MenuShop = ReplyKeyboardMarkup(resize_keyboard=True).add(btnEP, btnST, btnBack)

