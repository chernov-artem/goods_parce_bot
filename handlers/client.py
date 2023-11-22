import time

from aiogram import types, Dispatcher

import table_file
from create_bot import dp, bot
from keyboards.client_kb import *
from aiogram.types import ReplyKeyboardRemove
import parcing_functions


async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Готов к работе', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботов в ЛС. Напишите ему http://t.me/spb97192568_test_pizza_bot")

async def button1(messgage : types.Message):
    await bot.send_message(messgage.from_user.id, "тов1_5", reply_markup=kb_notebook1)
    # await parcing_functions.open_page("82X70045RK")
    await messgage.delete()

async def button2(message: types.Message):
    await bot.send_message(message.from_user.id, "тов6_10", reply_markup=kb_notebook2)
    await message.delete()

async def button3(message: types.Message):
    await bot.send_message(message.from_user.id, "тов11_15", reply_markup=kb_notebook3)
    await message.delete()

async def button4(message: types.Message):
    await bot.send_message(message.from_user.id, "тов11_15", reply_markup=kb_notebook4)
    await message.delete()

async def button5(message: types.Message):
    await bot.send_message(message.from_user.id, "тов11_15", reply_markup=kb_notebook5)
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

async def button_11sensor_screen(message: types.Message):
    await bot.send_message(message.from_user.id, "11 Сенсорный экран:\n" +table_file.sensor_screen)
    await message.delete()

async def button_12case_color(message: types.Message):
    await bot.send_message(message.from_user.id, "12 Цвет корпуса:\n" +table_file.case_color)
    await message.delete()

async def button_13weight(message: types.Message):
    await bot.send_message(message.from_user.id, "13 Вес:\n" +table_file.weight)
    await message.delete()

async def button_15proc_frequency(message: types.Message):
    await bot.send_message(message.from_user.id, "15 Частота процессора:\n" +table_file.proc_freq)
    await message.delete()

async def button_16video_card_full(message: types.Message):
    await bot.send_message(message.from_user.id, "16 Видеокарта:\n" +table_file.videocard_full)
    await message.delete()

async def button_17ddr_type(message: types.Message):
    await bot.send_message(message.from_user.id, "17 Тип памяти:\n" +table_file.ddr_type)
    await message.delete()

async def button_18ddr_freq(message: types.Message):
    await bot.send_message(message.from_user.id, "18 Частота памяти:\n" +table_file.ddr_freq)
    await message.delete()

async def button_19storage_conf(message: types.Message):
    await bot.send_message(message.from_user.id, "19 Конфигурация накопителей:\n" +table_file.storage_configuration)
    await message.delete()

async def button_20interfaces(message: types.Message):
    await bot.send_message(message.from_user.id, "20 Интерфейсы:\n" +table_file.interfaces)
    await message.delete()

async def button_21wireless_connection(message: types.Message):
    await bot.send_message(message.from_user.id, "21 беспроводная связь.\nпиши:\nWi-Fi и Bluetooth" +
                                                 "\nследующая строка просто для твоей информации \n" + table_file.wireless_connection +
                           "\n Версия bluetooth " + table_file.bluetooth + "\n Версия wi-fi " + table_file.wifi)
    await message.delete()

async def button_22optical(message: types.Message):
    await bot.send_message(message.from_user.id, "22 Оптический привод:\n" +table_file.optical)
    await message.delete()

async def button_23width(message: types.Message):
    await bot.send_message(message.from_user.id, "23 Ширина:\n" +table_file.width)
    await message.delete()

async def button_24depth(message: types.Message):
    await bot.send_message(message.from_user.id, "24 Глубина(длинна):\n" +table_file.depth)
    await message.delete()

async def button_25height(message: types.Message):
    await bot.send_message(message.from_user.id, "25 Высота:\n" +table_file.height)
    await message.delete()






def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(button1, commands=['тов1_5'])
    dp.register_message_handler(button2, commands=['тов6_10'])
    dp.register_message_handler(button3, commands=['тов11_15'])
    dp.register_message_handler(button4, commands=['тов16_20'])
    dp.register_message_handler(button5, commands=['тов21_25'])
    dp.register_message_handler(button_1screen, commands=['1_экран'])
    dp.register_message_handler(button_2proc, commands=['2_проц'])
    dp.register_message_handler(button_3os, commands=['3_Операционная_система'])
    dp.register_message_handler(button_4DDR, commands=['4_ОПЕР_память'])
    dp.register_message_handler(button_5HDD, commands=['5_Жесткий_диск'])
    dp.register_message_handler(button_6videocard, commands=['6_видеокарта'])
    dp.register_message_handler(button_7matrix, commands=['7_матрица_дисп'])
    dp.register_message_handler(button_8fingerprint, commands=['8_сканер_отпеч'])
    dp.register_message_handler(button_9keyboard_backlit, commands=['9_подсветка_клав'])
    dp.register_message_handler(button_10case_material, commands=['10_материал_корп'])
    dp.register_message_handler(button_11sensor_screen, commands=['11_сенсорный_экран'])
    dp.register_message_handler(button_12case_color, commands=['12_цвет_корпуса'])
    dp.register_message_handler(button_13weight, commands=['13_вес'])
    dp.register_message_handler(button_15proc_frequency, commands=['15_проц_частота'])
    dp.register_message_handler(button_16video_card_full, commands=['16_видеокарта_полн'])
    dp.register_message_handler(button_17ddr_type, commands=['17_тип_памяти'])
    dp.register_message_handler(button_18ddr_freq, commands=['18_частота_памяти'])
    dp.register_message_handler(button_19storage_conf, commands=['19_конф_накопит'])
    dp.register_message_handler(button_20interfaces, commands=['20_интерфейсы'])
    dp.register_message_handler(button_21wireless_connection, commands=['21_беспр_связь'])
    dp.register_message_handler(button_22optical, commands=['22_сдром'])
    dp.register_message_handler(button_23width, commands=['23_ширина'])
    dp.register_message_handler(button_24depth, commands=['24_глубина'])
    dp.register_message_handler(button_25height, commands=['25_толщина'])
