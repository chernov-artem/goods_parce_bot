from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Кнопка1')
b2 = KeyboardButton('/Кнопка2')
b3 = KeyboardButton('/1экран')
b4 = KeyboardButton('/2проц')
b5 = KeyboardButton('/3ОС')
b6 = KeyboardButton('/4ОПЕР_память')
b7 = KeyboardButton('/5Жесткий_диск')
b8 = KeyboardButton('/6видеокарта')
b9 = KeyboardButton('/7матрица_дисп')
b10 = KeyboardButton('/8сканер_отпеч')
b11 = KeyboardButton('/9подсветка_клав')
b12 = KeyboardButton('/10материал_корп')

b14 = KeyboardButton('/start')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).row(b3,b4,b5,b6,b7).row(b8,b9,b10,b11,b12).add(b14)
# kb_client.row(b1, b2, b3, b4)