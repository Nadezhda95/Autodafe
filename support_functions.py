from db import select_from_table


def cur_user_id_finder(user_id, login):
    if user_id:
        condition = "userID = '{}'".format(user_id)
        user_id = select_from_table('users', 'userID', condition)
        print('if')
    elif login:
        condition = "user = '{}'".format(login)
        user_id = select_from_table('users', 'userID', condition)
        print('elif')
    return user_id


def get_chat_ids():
    chats = select_from_table('chats_prod', 'chatID')
    return chats


def is_admin(login):
    condition = "login = '{}'".format(login)
    is_true = len(select_from_table('admins', 'login', condition)) == 1
    return is_true
