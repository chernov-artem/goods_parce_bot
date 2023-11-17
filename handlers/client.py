import time

from aiogram import types, Dispatcher

import table_file
from create_bot import dp, bot
from keyboards.client_kb import kb_client
from aiogram.types import ReplyKeyboardRemove
import parcing_functions


async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Готов к работе', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботов в ЛС. Напишите ему http://t.me/spb97192568_test_pizza_bot")

async def button1(messgage : types.Message):
    await bot.send_message(messgage.from_user.id, "Нажали кнопку 1")
    await parcing_functions.open_page("82X70045RK")
    await messgage.delete()

async def button2(message: types.Message):
    await parcing_functions.get_proc()
    await message.delete()

async def button_1screen(message: types.Message):
    await bot.send_message(message.from_user.id, "1 экран:\n" + table_file.screen)
    await message.delete()

async def button_2proc(message: types.Message):
    await bot.send_message(message.from_user.id, "2 процессор:\n" + table_file.processor)
    await message.delete()

async def button_3os(message: types.Message):
    await bot.send_message(message.from_user.id, "3 оперативная система:\n" + table_file.oper_sist)
    await message.delete()

async def button_4DDR(message: types.Message):
    await bot.send_message(message.from_user.id, "4 оперативная память:\n" +table_file.ddr)
    await message.delete()

async def button_5HDD(message: types.Message):
    await bot.send_message(message.from_user.id, "5 жесткий диск:\n" +table_file.hdd)
    await message.delete()

async def button_6videocard(message: types.Message):
    await bot.send_message(message.from_user.id, "6 видеокарта:\n" +table_file.videocard)
    await message.delete()

async def button_7matrix(message: types.Message):
    await bot.send_message(message.from_user.id, "7 матрица дисплея:\n" +table_file.matrix)
    await message.delete()

async def button_8fingerprint(message: types.Message):
    await bot.send_message(message.from_user.id, "8 сканер отпечатка пальца:\n" +table_file.fingerprint)
    await message.delete()

async def button_9keyboard_backlit(message: types.Message):
    await bot.send_message(message.from_user.id, "9 Подсветка клавиатуры:\n" +table_file.keyboard_backlit)
    await message.delete()

async def button_10case_material(message: types.Message):
    await bot.send_message(message.from_user.id, "10 материал корпуса:\n" +table_file.case_material)
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(button1, commands=['Кнопка1'])
    dp.register_message_handler(button2, commands=['Кнопка2'])
    dp.register_message_handler(button_1screen, commands=['1экран'])
    dp.register_message_handler(button_2proc, commands=['2проц'])
    dp.register_message_handler(button_3os, commands=['3ОС'])
    dp.register_message_handler(button_4DDR, commands=['4ОПЕР_память'])
    dp.register_message_handler(button_5HDD, commands=['5Жесткий_диск'])
    dp.register_message_handler(button_6videocard, commands=['6видеокарта'])
    dp.register_message_handler(button_7matrix, commands=['7матрица_дисп'])
    dp.register_message_handler(button_8fingerprint, commands=['8сканер_отпеч'])
    dp.register_message_handler(button_9keyboard_backlit, commands=['9подсветка_клав'])
    dp.register_message_handler(button_10case_material, commands=['10материал_корп'])

