from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bstart = KeyboardButton('/start')
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




kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_notebook1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_notebook2 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(bstart)
kb_notebook1.row(b3,b4).row(b5,b6,b7).add(bstart)
kb_notebook2.row(b8,b9).row(b10,b11,b12).add(bstart)
# kb_notebook2.row(b,b).row(b,b,b).add(bstart)
# kb_notebook2.row(b,b).row(b,b,b).add(bstart)

# kb_client.row(b1, b2, b3, b4)