from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Кнопка1')
b2 = KeyboardButton('/Кнопка2')
b3 = KeyboardButton('/Кнопка3')
b14 = KeyboardButton('/start')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3).add(b14)
# kb_client.row(b1, b2, b3, b4)