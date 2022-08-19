#!/usr/bin/env python
from aiogram import Bot, Dispatcher, types, executor

from db import insert_list_into_table
from support_functions import cur_user_id_finder, get_chat_ids
from dotenv import load_dotenv, dotenv_values
load_dotenv()
import os

token = os.environ.get("api-token")

config = dotenv_values(".env")
bot = Bot(config.get('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Bot started')

@dp.message_handler(commands=['link'])
async def add_chat(message: types.Message):
    print(message.chat.id)
    print(message.chat.title)
    insert_list_into_table([message.chat.id, message.chat.title], 'chats_prod', ('chatID', 'chat_name'))
    await message.answer('Чат успешно добавлен')

@dp.message_handler(commands=['ban'])
async def kick_user(message: types.Message):
    if message.from_user.username == 'SerDenis' or message.from_user.username == 'brainwashed_from_rock':
        user_to_ban = message.text.split("/ban ", 1)[1]
        user_id = cur_user_id_finder(user_to_ban)[0][0]
        print(user_id)
        chat_ids = get_chat_ids()
        for i in range(len(chat_ids)):
            try:
                await bot.kick_chat_member(chat_id=chat_ids[i][0], user_id=user_id)
            except:
                continue


executor.start_polling(dp, skip_updates=True)