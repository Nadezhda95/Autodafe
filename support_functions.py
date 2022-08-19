from db import select_from_table


def cur_user_id_finder(login):
    condition = "user = '{}'".format(login)
    user_id = select_from_table('users', 'userID', condition)
    return user_id


def get_chat_ids():
    chats = select_from_table('chats_prod', 'chatID')
    return chats




