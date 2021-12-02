from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton("Главное меню")
btnBack = KeyboardButton("Назад")

# Main menu
btnGameSteam = KeyboardButton("Игры Steam")
btnGameEG = KeyboardButton("Игры Epic Games")
btnInfo = KeyboardButton("Информация")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGameSteam, btnGameEG, btnInfo)

# Steam button
btnFreeGameS = KeyboardButton("Бесплатные игры Steam")
btnDiscountGameS = KeyboardButton("Игры со скидкой")
btnDFGameS = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFreeGameS, btnDiscountGameS, btnBack)

# Epic Games button
btnFreeGameEG = KeyboardButton("Бесплатные игры Epic Games")
btnDiscountGameEG = KeyboardButton("Игры со скидкой")
btnDFGameEG = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFreeGameEG, btnDiscountGameEG, btnBack)

# Other Menu
btnShop = KeyboardButton("Магазины")
btnBot = KeyboardButton("Наши боты")
btnWS = KeyboardButton("Наш сайт")
btnDev = KeyboardButton("Разработчик")
MenuOther = ReplyKeyboardMarkup(resize_keyboard=True).add(btnShop, btnBot, btnWS, btnDev, btnMain)

# Menu Shop
btnEP = KeyboardButton("Магазин Epic Games")
btnST = KeyboardButton("Магазин Steam")
MenuShop = ReplyKeyboardMarkup(resize_keyboard=True).add(btnEP, btnST, btnBack)

btnFreeTest = KeyboardButton("Игры")
testBtn = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFreeTest, btnBack)

