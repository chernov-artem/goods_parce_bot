import time
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

import table_file
from create_bot import dp, bot
from keyboards.client_kb import *
from aiogram.types import ReplyKeyboardRemove
import parcing_functions

class FSM_goods(StatesGroup):
    good = State()




async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Готов к работе', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботов в ЛС. Напишите ему http://t.me/spb97192568_test_pizza_bot")

async def cm_start(message : types.Message):
    await bot.send_message(message.from_user.id, "функция работает")
    await FSM_goods.good.set()

async def load_good(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['good'] = message.text
    await message.reply("товар загружен " + data["good"])
    new_good = data['good']
    print(new_good)
    parcing_functions.get_good_data(new_good)
    time.sleep(15)
    await bot.send_message(message.from_user.id, 'новый товар доступен')
    await state.finish()

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

async def button_1item(message: types.Message):
    await bot.send_message(message.from_user.id, "1 пункт:\n" + table_file.item1)
    await message.delete()

async def button_2item(message: types.Message):
    await bot.send_message(message.from_user.id, "2 пункт:\n" + table_file.item2)
    await message.delete()

async def button_3item(message: types.Message):
    await bot.send_message(message.from_user.id, "3 пункт:\n" + table_file.item3)
    await message.delete()

async def button_4item(message: types.Message):
    await bot.send_message(message.from_user.id, "4 пункт:\n" + table_file.item4)
    await message.delete()

async def button_5item(message: types.Message):
    await bot.send_message(message.from_user.id, "5 пункт:\n" + table_file.item5)
    await message.delete()

async def button_6item(message: types.Message):
    await bot.send_message(message.from_user.id, "6 пункт:\n" + table_file.item6)
    await message.delete()

async def button_7item(message: types.Message):
    await bot.send_message(message.from_user.id, "7 пункт:\n" +table_file.item7)
    await message.delete()

async def button_8item(message: types.Message):
    await bot.send_message(message.from_user.id, "8 пункт:\n" + table_file.item8)
    await message.delete()

async def button_9item(message: types.Message):
    await bot.send_message(message.from_user.id, "9 пункт:\n" + table_file.item9)
    await message.delete()

async def button_10item(message: types.Message):
    await bot.send_message(message.from_user.id, "10 пункт:\n" + table_file.item10)
    await message.delete()

async def button_11item(message: types.Message):
    await bot.send_message(message.from_user.id, "11 пункт:\n" + table_file.item11)
    await message.delete()

async def button_12item(message: types.Message):
    await bot.send_message(message.from_user.id, "12 пункт:\n" + table_file.item12)
    await message.delete()

async def button_13item(message: types.Message):
    await bot.send_message(message.from_user.id, "13 пункт:\n" + table_file.item13)
    await message.delete()

async def button_14item(message: types.Message):
    await bot.send_message(message.from_user.id, "14 пункт:\n" + table_file.item14)
    await message.delete()

async def button_15item(message: types.Message):
    await bot.send_message(message.from_user.id, "15 пункт:\n" + table_file.item15)
    await message.delete()

async def button_16item(message: types.Message):
    await bot.send_message(message.from_user.id, "16 пункт:\n" + table_file.item16)
    await message.delete()

async def button_17item(message: types.Message):
    await bot.send_message(message.from_user.id, "17 пункт:\n" + table_file.item17)
    await message.delete()

async def button_18item(message: types.Message):
    await bot.send_message(message.from_user.id, "18 пункт:\n" + table_file.item18)
    await message.delete()

async def button_19item(message: types.Message):
    await bot.send_message(message.from_user.id, "19 пункт:\n" + table_file.item19)
    await message.delete()

async def button_20item(message: types.Message):
    await bot.send_message(message.from_user.id, "20 пункт:\n" + table_file.item20)
    await message.delete()

async def button_21item(message: types.Message):
    await bot.send_message(message.from_user.id, "21 пункт:\n" + table_file.item21)
    await message.delete()

async def button_22item(message: types.Message):
    await bot.send_message(message.from_user.id, "22 пункт:\n" + table_file.item22)
    await message.delete()

async def button_23item(message: types.Message):
    await bot.send_message(message.from_user.id, "23 пункт:\n" + table_file.item23)
    await message.delete()

async def button_24item(message: types.Message):
    await bot.send_message(message.from_user.id, "24 пункт:\n" + table_file.item24)
    await message.delete()

async def button_25item(message: types.Message):
    await bot.send_message(message.from_user.id, "25 пункт:\n" + table_file.item25)
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(cm_start, commands=['Загрузить'])
    dp.register_message_handler(load_good, state=FSM_goods.good)
    dp.register_message_handler(button1, commands=['тов1_5'])
    dp.register_message_handler(button2, commands=['тов6_10'])
    dp.register_message_handler(button3, commands=['тов11_15'])
    dp.register_message_handler(button4, commands=['тов16_20'])
    dp.register_message_handler(button5, commands=['тов21_25'])
    dp.register_message_handler(button_1item, commands=['1_пункт'])
    dp.register_message_handler(button_2item, commands=['2_пункт'])
    dp.register_message_handler(button_3item, commands=['3_пункт'])
    dp.register_message_handler(button_4item, commands=['4_пункт'])
    dp.register_message_handler(button_5item, commands=['5_пункт'])
    dp.register_message_handler(button_6item, commands=['6_пункт'])
    dp.register_message_handler(button_7item, commands=['7_пункт'])
    dp.register_message_handler(button_8item, commands=['8_пункт'])
    dp.register_message_handler(button_9item, commands=['9_пункт'])
    dp.register_message_handler(button_10item, commands=['10_пункт'])
    dp.register_message_handler(button_11item, commands=['11_пункт'])
    dp.register_message_handler(button_12item, commands=['12_пункт'])
    dp.register_message_handler(button_13item, commands=['13_пункт'])
    dp.register_message_handler(button_14item, commands=['14_пункт'])
    dp.register_message_handler(button_15item, commands=['15_пункт'])
    dp.register_message_handler(button_16item, commands=['16_пункт'])
    dp.register_message_handler(button_17item, commands=['17_пункт'])
    dp.register_message_handler(button_18item, commands=['18_пункт'])
    dp.register_message_handler(button_19item, commands=['19_пункт'])
    dp.register_message_handler(button_20item, commands=['20_пункт'])
    dp.register_message_handler(button_21item, commands=['21_пункт'])
    dp.register_message_handler(button_22item, commands=['22_пункт'])
    dp.register_message_handler(button_23item, commands=['23_пункт'])
    dp.register_message_handler(button_24item, commands=['24_пункт'])
    dp.register_message_handler(button_25item, commands=['25_пункт'])
