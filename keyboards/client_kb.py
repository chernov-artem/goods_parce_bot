from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Кнопка1')
b2 = KeyboardButton('/Кнопка2')
b3 = KeyboardButton('/1экран')
b4 = KeyboardButton('/2проц')
b5 = KeyboardButton('/3ОС')
b6 = KeyboardButton('/4ОПЕР_память')
b7 = KeyboardButton('/5Жесткий_диск')
b14 = KeyboardButton('/start')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).row(b3,b4,b5,b6,b7).add(b14)
# kb_client.row(b1, b2, b3, b4)