from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bstart = KeyboardButton('/start')
b001 = KeyboardButton('/Кнопка1')
b002 = KeyboardButton('/Кнопка2')
b003 = KeyboardButton('/Кнопка3')
b004 = KeyboardButton('/Кнопка4')
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
b13 = KeyboardButton('/11сенсорный_экран')
b14 = KeyboardButton('/12цвет_корпуса')
b15 = KeyboardButton('/13вес')
b16 = KeyboardButton('/14габариты_ШхДхВ')
b17 = KeyboardButton('/2проц')
b18 = KeyboardButton('/16проц_частота')
b19 = KeyboardButton('/17видеокарта_полн')
b20 = KeyboardButton('/18типа_памяти')
b21 = KeyboardButton('/19частота_памяти')
b22 = KeyboardButton('/20конфигурация_накопит')
# b2 = KeyboardButton('/2')




kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_notebook1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_notebook2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_notebook3 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b001).add(b002).add(bstart)
kb_notebook1.row(b3,b4).row(b5,b6,b7).add(bstart)
kb_notebook2.row(b8,b9).row(b10,b11,b12).add(bstart)
# kb_notebook2.row(b,b).row(b,b,b).add(bstart)
# kb_notebook2.row(b,b).row(b,b,b).add(bstart)

# kb_client.row(b1, b2, b3, b4)