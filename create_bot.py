from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token="6676930898:AAH51NmUt_5iUOlV7RDahTemSivDe5BxKrs")
dp = Dispatcher(bot, storage=storage)