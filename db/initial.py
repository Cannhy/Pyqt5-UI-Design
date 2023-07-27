import os.path
import sqlite3

database_name = '航味食堂'  # 数据库名


def get_data_path(name):
    this_dir = os.path.dirname(__file__)
    result = this_dir + '_dir/' + name + '.db'
    return result


def get_data_dir_path(name):
    this_dir = os.path.dirname(__file__)
    result = this_dir + '_dir'
    return result


def initial():
    data_path = get_data_path(database_name)
    data_dir_path = get_data_dir_path(database_name)
    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)         # 创建路径
    if not os.path.exists(data_path):
        connect = sqlite3.connect(data_path)
        cursor = connect.cursor()
        # 设置菜谱表单
        sql = 'CREATE TABLE dish_menu(' \
              "name nvarchar(50) not null DEFAULT '', " \
              "canteen nvarchar(50) not null DEFAULT '', " \
              "counter nvarchar(50) not null DEFAULT '', " \
              "price nvarchar(50) not null DEFAULT '', " \
              "times nvarchar(20) not null DEFAULT '', " \
              "num int not null DEFAULT 0, " \
              "taste nvarchar(50) not null DEFAULT '', " \
              "nutrition nvarchar(50) not null DEFAULT '', " \
              "dish_id integer PRIMARY KEY autoincrement)"
        cursor.execute(sql)
        sql = 'CREATE TABLE canteen_counter(' \
              "canteen nvarchar(50) not null DEFAULT '', " \
              "counter nvarchar(100) not null DEFAULT '')"
        cursor.execute(sql)
        sql = 'CREATE TABLE comments(' \
              "comment_id integer primary key autoincrement, " \
              "sender varchar(50) not null DEFAULT '', " \
              "types int not null, " \
              "receiver varchar(50) not null DEFAULT '', " \
              "times varchar(50) not null DEFAULT '', " \
              "content varchar(100) not null DEFAULT '', " \
              "persons varchar(128) not null DEFAULT '', " \
              "num int not null DEFAULT 0)"
        cursor.execute(sql)
        add_canteen_counter(connect, cursor)
        sql = 'CREATE TABLE user(name varchar(25) primary key  not null, ' \
              'password varchar(25) not null)'
        cursor.execute(sql)
        add_comment(connect, cursor)
        # 载入题库
        add_dish_menu(connect, cursor)
        connect.commit()
    return data_path


def destroy_database():
    data_path = get_data_path(database_name)
    if os.path.exists(data_path):
        os.remove(data_path)


def get_base():
    this_dir = os.path.dirname(__file__)
    result = this_dir + '_data/dish.db'
    return result


def get_key_str(key_list):
    key_str = '(' + key_list[0]
    for i in range(1, len(key_list)):
        key_str = key_str + ',' + key_list[i]
    key_str = key_str + ')'
    return key_str


def get_table(table_name):
    conn = sqlite3.connect(get_base())
    cur = conn.cursor()
    sql = "SELECT * FROM %s" % table_name
    cur.execute(sql)
    return cur.fetchall()


def get_question(t):
    s = t[0] + '\n' + 'A.' + t[1] + '\n' + 'B.' + t[2] + '\n' + 'C.' + t[3] + '\n' + 'D.' + t[4]
    return s


def add_dish_menu(connect, cursor):
    key_list = ('name', 'canteen', 'counter', 'price', 'times', 'num', 'taste', 'nutrition', 'dish_id')
    t1 = get_table('dish_menu')
    for t in t1:
        name = t[0]
        canteen = t[1]
        counter = t[2]
        price = t[3]
        times = t[4]
        num = t[5]
        taste = t[6]
        nutrition = t[7]
        dish_id = t[8]
        value_str = "('%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%d')" %\
                    (name, canteen, counter, price, times, num, taste, nutrition, dish_id)
        sql = 'INSERT INTO %s %s VALUES %s' % ('dish_menu', get_key_str(key_list), value_str)
        cursor.execute(sql)
        connect.commit()


def add_canteen_counter(connect, cursor):
    key_list = ('canteen', 'counter')
    t1 = get_table('canteen_counter')
    for t in t1:
        canteen = t[0]
        counter = t[1]
        value_str = "('%s', '%s')" % (canteen, counter)
        sql = 'INSERT INTO %s %s VALUES %s' % ('canteen_counter', get_key_str(key_list), value_str)
        cursor.execute(sql)
        connect.commit()


def add_comment(connect, cursor):
    key_list = ('comment_id', 'sender', 'types', 'receiver', 'times', 'content', 'persons', 'num')
    t1 = get_table('comments')
    for t in t1:
        comment_id = t[0]
        sender = t[1]
        types = t[2]
        receiver = t[3]
        times = t[4]
        content = t[5]
        persons = t[6]
        num = t[7]
        value_str = "('%s', '%s', '%s', '%s', '%s', '%s', '%s', %d)" % (comment_id, sender, types, receiver, times, content, persons, num)
        sql = 'INSERT INTO %s %s VALUES %s' % ('comments', get_key_str(key_list), value_str)
        cursor.execute(sql)
        connect.commit()
