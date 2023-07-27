import os

import sqlite3

data_path = ''


def get_key_str(key_list):
    key_str = '(' + key_list[0]
    for i in range(1, len(key_list)):
        key_str = key_str + ',' + key_list[i]
    key_str = key_str + ')'
    return key_str


def get_value_str(value_list):
    s = '('
    if len(value_list) > 1:
        for value in value_list:
            if type(value) is str:
                s = s + "'%s', " % value
            else:
                s = s + '%s, ' % str(value)
        s = s[:-2] + ')'
    else:
        value = value_list[0]
        if type(value) is str:
            s = "('%s')" % value
        else:
            s = '(%s)' % str(value)
    return s


def get_database_path(name):
    this_dir = os.path.dirname(__file__)
    result = this_dir + '_dir/' + name + '.db'
    return result


nutritionDic = {'碳水': 0, '肉类': 1, '蔬菜': 2}
tasteDic = {'麻辣': 0, '清淡': 1, '酸辣': 2, '香辣': 3, '酱香': 4, '甜味': 5, '酸甜': 6, '酸咸': 7, '甜咸': 8, '咸香': 9}


class DB:
    _instance = None
    _flag = False

    def __init__(self):
        if not DB._flag:
            self.database_path = data_path
            self.connect = sqlite3.connect(self.database_path)
            self.cursor = self.connect.cursor()
            DB._flag = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_table(self, table_name, key_list, type_list):
        sql = 'CREATE TABLE %s (' % table_name
        sql = sql + key_list[0] + ' ' + type_list[0]
        for i in range(1, len(key_list)):
            sql = sql + ', ' + key_list[i] + ' ' + type_list[i]
        sql = sql + ')'
        self.cursor.execute(sql)
        self.connect.commit()

    def insert(self, table_name, key_list, value_list):
        sql = 'INSERT INTO %s %s VALUES %s' % (table_name, get_key_str(key_list), get_value_str(value_list))
        self.cursor.execute(sql)
        self.connect.commit()

    def change(self, table_name, find_key, find_key_value, key, new_value):
        sql = "UPDATE %s SET %s = '%s' WHERE %s = '%s'" % (table_name, key, new_value, find_key, find_key_value)
        self.cursor.execute(sql)
        self.connect.commit()

    def get_table(self, table_name):
        sql = 'SELECT * FROM %s' % table_name
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def find_key(self, table_name, key, value, _type):
        sql = ''
        if _type == 'str':
            sql = "SELECT * FROM %s WHERE %s= '%s'" % (table_name, key, value)
        elif _type == 'int':
            sql = "SELECT * FROM %s WHERE %s= %d" % (table_name, key, value)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def present_search(self, canteenKey, counterKey):
        sql = "SELECT * FROM dish_menu WHERE canteen= '%s' and counter= '%s'" % (canteenKey, counterKey)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def canteen_counter_search(self):
        sql = "SELECT * FROM canteen_counter"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def counter_alive(self, cant: str, coun: str):
        sql = "SELECT * FROM canteen_counter WHERE canteen= '%s'" % cant
        self.cursor.execute(sql)
        tmp = self.cursor.fetchall()
        if coun in tmp[0][1].split():
            return True, tmp
        else:
            return False, tmp

    def present_add(self, text: str, tYpe):
        if tYpe == 1:
            sql = "INSERT INTO canteen_counter VALUES ('%s', '')" % text
            self.cursor.execute(sql)
            self.connect.commit()
        if tYpe == 2:
            flag, tmp = self.counter_alive(text.split()[0], text.split()[1])
            if flag:
                return True
            else:
                sql = "UPDATE canteen_counter SET counter= '%s' WHERE canteen= '%s'" % (
                tmp[0][1] + ' ' + text.split()[1], text.split()[0])
                self.cursor.execute(sql)
                self.connect.commit()
                return False
        if tYpe == 3:
            spt = text.split()
            sql = "INSERT INTO dish_menu (name, canteen, counter, price, times, taste, nutrition) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            spt[0], spt[1], spt[2], spt[3], spt[4], spt[5], spt[6])
            self.cursor.execute(sql)
            self.connect.commit()

    def present_del(self, text: str, tYpe):
        if tYpe == 1:
            sql = "DELETE FROM canteen_counter WHERE canteen= '%s'" % text
            self.cursor.execute(sql)
            self.connect.commit()
        if tYpe == 2:
            flag, tmp = self.counter_alive(text.split()[0], text.split()[1])
            res = str(tmp[0][1]).split()
            res.remove(text.split()[1])
            sql = "UPDATE canteen_counter SET counter= '%s' WHERE canteen= '%s'" % (" ".join(res), text.split()[0])
            self.cursor.execute(sql)
            self.connect.commit()
        if tYpe == 3:
            sql = 'select * FROM dish_menu where dish_id=%d' % int(text)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            if len(res) == 0:
                return False
            else:
                sql = "DELETE FROM dish_menu where dish_id= %d" % int(text)
                self.cursor.execute(sql)
                self.connect.commit()
                return True

    def present_fix(self, key, value, ID: int):
        sql = "UPDATE dish_menu SET %s= '%s' WHERE dish_id = %d" % (key, value, ID)
        self.cursor.execute(sql)
        self.connect.commit()

    def get_content(self):
        des = 'comments'
        sql = "select * FROM %s" % des
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert_comment(self, item):
        sql = "INSERT INTO comments (sender, types, receiver, times, content) VALUES ('%s', %d, '%s', '%s', '%s')" % \
              (item['uname'], item['type'], item['receiver'], item['create_time'], item['content'])
        self.cursor.execute(sql)
        self.connect.commit()
        sql = "SELECT * FROM comments"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res[len(res) - 1][0]

    def update_comment(self, name, type, likenum, id):
        sql = "UPDATE comments SET num= %d where comment_id= %d" % (likenum, id)
        self.cursor.execute(sql)
        self.connect.commit()
        sql = "SELECT * FROM comments WHERE comment_id= %d" % id
        self.cursor.execute(sql)
        res = str(list(self.cursor.fetchall()[0])[6]).split()
        if type == 1:
            res.append(name)
        else:
            res.remove(name)
        sql = "UPDATE comments SET persons= '%s' where comment_id= %d" % (" ".join(res), id)
        self.cursor.execute(sql)
        self.connect.commit()

    def get_canteens(self):
        sql = "SELECT * FROM canteen_counter"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        des = [i[0] for i in res]
        return des

    def get_counters(self, canteen):
        sql = "SELECT * FROM canteen_counter WHERE canteen= '%s'" % canteen
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return str(res[0][1]).split()

    def get_dishes(self, canteen, counter):
        sql = "SELECT * FROM dish_menu WHERE canteen= '%s' and counter= '%s'" % (canteen, counter)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        des = [i[0] for i in res]
        return des

    def insert_record(self, key_list: list, name):
        table = name + '_record'
        sql = "INSERT INTO %s VALUES ('%s', '%s', '%s', '%s', '%s', %d)" % (
        table, key_list[0], key_list[1], key_list[2], key_list[3], key_list[4], key_list[5])
        self.cursor.execute(sql)
        self.connect.commit()

    def add_eaten_time(self, key_list, name):
        sql = "SELECT * FROM dish_menu WHERE canteen= '%s' and counter= '%s' and name= '%s'" % (
        key_list[0], key_list[1], key_list[2])
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        sql = "UPDATE dish_menu SET num= %d WHERE canteen= '%s' and counter= '%s' and name= '%s'" % (
        res[0][5] + 1, key_list[0], key_list[1], key_list[2])
        self.cursor.execute(sql)
        self.connect.commit()
        table = name + '_frequency'
        sql = "SELECT * FROM %s WHERE canteen= '%s' and counter= '%s' and name= '%s'" % (table,
            key_list[0], key_list[1], key_list[2])
        self.cursor.execute(sql)
        res2 = self.cursor.fetchall()
        if len(res2) == 0:
            sql = "INSERT INTO %s VALUES ('%s', '%s', '%s', '%s', '%s', 1)" % (table, res[0][1], res[0][2], res[0][0], res[0][6], res[0][7])
            self.cursor.execute(sql)
            self.connect.commit()
        else:
            sql = "UPDATE %s SET num= %d WHERE canteen= '%s' and counter= '%s' and name= '%s'" % (table,
                res2[0][5] + 1, key_list[0], key_list[1], key_list[2])
            self.cursor.execute(sql)
            self.connect.commit()
        if res[0][7] != '饮品':
            table = name + '_nutrition'
            sql = "SELECT * FROM %s" % table
            self.cursor.execute(sql)
            res3 = self.cursor.fetchall()
            if len(res3) != 0:
                res3 = list(res3[0])
                sql = "DELETE FROM %s" % table
                self.cursor.execute(sql)
                self.connect.commit()
                res3[nutritionDic[res[0][7]]] += 1
                sql = "INSERT INTO %s VALUES (%d, %d, %d)" % (table, res3[0], res3[1], res3[2])
                self.cursor.execute(sql)
                self.connect.commit()
            else:
                res3 = [0, 0, 0]
                res3[nutritionDic[res[0][7]]] = 1
                sql = "INSERT INTO %s VALUES (%d, %d, %d)" % (table, res3[0], res3[1], res3[2])
                self.cursor.execute(sql)
                self.connect.commit()
        if res[0][7] != '饮品':
            table = name + '_taste'
            sql = "SELECT * FROM %s" % table
            self.cursor.execute(sql)
            res4 = self.cursor.fetchall()
            if len(res4) != 0:
                res4 = list(res4[0])
                sql = "DELETE FROM %s" % table
                self.cursor.execute(sql)
                self.connect.commit()
                res4[tasteDic[res[0][6]]] += 1
                sql = "INSERT INTO %s VALUES (%d, %d, %d, %d, %d, %d, %d, %d, %d, %d)" % (
                table, res4[0], res4[1], res4[2], res4[3], res4[4], res4[5], res4[6], res4[7], res4[8], res4[9])
                self.cursor.execute(sql)
                self.connect.commit()
            else:
                res4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                res4[tasteDic[res[0][6]]] += 1
                sql = "INSERT INTO %s VALUES (%d, %d, %d, %d, %d, %d, %d, %d, %d, %d)" % (
                table, res4[0], res4[1], res4[2], res4[3], res4[4], res4[5], res4[6], res4[7], res4[8], res4[9])
                self.cursor.execute(sql)
                self.connect.commit()

    def sub_eaten_time(self, key_lists, name):
        for key_list in key_lists:
            sql = "SELECT * FROM dish_menu WHERE canteen= '%s' and counter= '%s' and name= '%s'" % (
                key_list[0], key_list[1], key_list[2])
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            sql = "UPDATE dish_menu SET num= %d WHERE canteen= '%s' and counter= '%s' and name= '%s'" % (
                res[0][5] - 1, key_list[0], key_list[1], key_list[2])
            self.cursor.execute(sql)
            self.connect.commit()
            table = name + '_frequency'
            sql = "SELECT * FROM %s WHERE canteen= '%s' and counter= '%s' and name= '%s'" % (table,
                                                                                             key_list[0], key_list[1],
                                                                                             key_list[2])
            self.cursor.execute(sql)
            res2 = self.cursor.fetchall()
            if res2[0][5] == 1:
                sql = "DELETE FROM %s WHERE canteen= '%s' and counter= '%s' and name= '%s'" % (table, key_list[0], key_list[1], key_list[2])
                self.cursor.execute(sql)
                self.connect.commit()
            else:
                sql = "UPDATE %s SET num= %d WHERE canteen= '%s' and counter= '%s' and name= '%s'" % (table, res2[0][5] - 1, key_list[0], key_list[1], key_list[2])
                self.cursor.execute(sql)
                self.connect.commit()
            if res[0][7] != '饮品':
                table = name + '_nutrition'
                sql = "SELECT * FROM %s" % table
                self.cursor.execute(sql)
                res3 = self.cursor.fetchall()
                res3 = list(res3[0])
                sql = "DELETE FROM %s" % table
                self.cursor.execute(sql)
                self.connect.commit()
                res3[nutritionDic[res[0][7]]] -= 1
                sql = "INSERT INTO %s VALUES (%d, %d, %d)" % (table, res3[0], res3[1], res3[2])
                self.cursor.execute(sql)
                self.connect.commit()

                table = name + '_taste'
                sql = "SELECT * FROM %s" % table
                self.cursor.execute(sql)
                res4 = self.cursor.fetchall()
                res4 = list(res4[0])
                sql = "DELETE FROM %s" % table
                self.cursor.execute(sql)
                self.connect.commit()
                res4[tasteDic[res[0][6]]] -= 1
                sql = "INSERT INTO %s VALUES (%d, %d, %d, %d, %d, %d, %d, %d, %d, %d)" % (
                    table, res4[0], res4[1], res4[2], res4[3], res4[4], res4[5], res4[6], res4[7], res4[8], res4[9])
                self.cursor.execute(sql)
                self.connect.commit()

    def getFreq(self, name):
        table = name + '_frequency'
        sql = "SELECT * FROM %s ORDER BY num DESC" % table
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getNutri(self, name):
        table = name + '_nutrition'
        sql = "SELECt * FROM %s" % table
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getTaste(self, name):
        table = name + '_taste'
        sql = "SELECt * FROM %s" % table
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def generateDish(self, nutri, taste):
        ans = []
        ans_addit = []
        for tas in range(len(taste) - 7):
            sql = "SELECT * FROM dish_menu WHERE nutrition= '%s' and taste= '%s' and times= '午餐' ORDER BY num DESC" % (nutri[0], taste[tas])
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for row in range(len(res)):
                temp = [res[row][0], res[row][1], res[row][2]]
                if row >= 3:
                    ans_addit.append(temp)
                else:
                    ans.append(temp)
                    ans_addit.append(temp)
        if len(ans) < 9:
            while len(ans) < 9:
                ans.append(ans_addit[len(ans)])
        return ans

    def get_record(self, name):
        table = name + '_record'
        sql = "SELECT * FROM %s" % table
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def delete_record(self, key_list, name):
        table = name + '_record'
        for ids in key_list:
            sql = "DELETE FROM %s where ID= %d" % (table, ids)
            self.cursor.execute(sql)
            self.connect.commit()

    def fix_record(self, name, key, value, ID: int):
        table = name + '_record'
        sql = "UPDATE %s SET %s= '%s' WHERE ID = %d" % (table, key, value, ID)
        self.cursor.execute(sql)
        self.connect.commit()

    def get_marks(self, name):
        table = name + '_mark'
        sql = "SELECT * FROM %s" % table
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert_mark(self, name, key_list):
        table = name + '_mark'
        sql = "INSERT INTO %s VALUES (%d, '%s', '%s')" % (table, key_list[0], key_list[1], key_list[2])
        self.cursor.execute(sql)
        self.connect.commit()

    def delete_mark(self, key_list, name):
        table = name + '_mark'
        for ids in key_list:
            sql = "DELETE FROM %s where ID= %d" % (table, ids)
            self.cursor.execute(sql)
            self.connect.commit()

    def fix_mark(self, name, key, value, ID: int):
        table = name + '_mark'
        sql = "UPDATE %s SET %s= '%s' WHERE ID = %d" % (table, key, value, ID)
        self.cursor.execute(sql)
        self.connect.commit()

    def get_des_eat(self, num: int):
        sql = "SELECT * FROM dish_menu order by num desc"
        self.cursor.execute(sql)
        return self.cursor.fetchmany(num)

    def delete_data(self, table_name, key, value):
        sql = "DELETE FROM %s where %s= '%s'" % (table_name, key, value)
        self.cursor.execute(sql)
        self.connect.commit()

    def delete_table(self, table_name):
        sql = 'DROP TABLE IF EXISTS %s' % table_name
        self.cursor.execute(sql)
        self.connect.commit()
