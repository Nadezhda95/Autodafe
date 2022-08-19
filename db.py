import sqlite3
import pandas as pd

conn = sqlite3.connect("autodafe.db")
cur = conn.cursor()


def create_table(name, columns):
    # columns = (user text, userID text)
    cur.execute('''
        CREATE TABLE {0}
        {1}
    '''.format(name, columns))
    conn.commit()
    conn.close()


# create_table('chats', '(chatID,chat_name)')


def insert_file_into_table(file_name, table, columns):
    conn = sqlite3.connect("autodafe.db")
    cur = conn.cursor()

    data = pd.read_table(file_name)
    # data = pd.read_csv(values)
    df = pd.DataFrame(data)

    for row in range(len(df.index.values)):
        cur.execute("""INSERT INTO {0} {1} VALUES (?,?)""".format(table, columns), df.values[row])
        conn.commit()
    conn.close()


# insert_into_table('chats.tsv', 'chats', '(chatID,chat_name)')


def insert_list_into_table(values, table, columns):
    conn = sqlite3.connect("autodafe.db")
    cur = conn.cursor()

    cur.execute("""INSERT INTO {0} {1} VALUES (?,?)""".format(table, columns), values)
    print('Inserted successfully {0}'.format(values))
    conn.commit()

    conn.close()


def select_from_table(table, columns, conditions=''):
    conn = sqlite3.connect("autodafe.db")
    cur = conn.cursor()
    if conditions == '':
        print("""SELECT {1} FROM {0}""".format(table, columns))
        cur.execute("""SELECT {1} FROM {0} """.format(table, columns))
    else:
        print("""SELECT {1} FROM {0} WHERE {2} """.format(table, columns, conditions))
        cur.execute("""SELECT {1} FROM {0} WHERE {2} """.format(table, columns, conditions))
    sql = cur.fetchall()
    # conn.commit()
    conn.close()
    return sql


#print(select_from_table('admins', 'login'))


def drop_table(table):
    cur.execute('''DROP TABLE {0}'''.format(table))
    conn.commit()
    conn.close()


# drop_table('users')

def delete_row(userID):
    cur.execute("""DELETE FROM users where userID=? """, (userID,))
    sql = cur.fetchone()
    conn.commit()
    conn.close()

# delete_row(956124349.0)
