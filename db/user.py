from db.DB import DB
import random


def check_same(table_name, key, value, _type):
    db = DB()
    if len(db.find_key(table_name, key, value, _type)) == 0:
        return False
    return True


class User:
    _instance = None
    _flag = False

    def __init__(self):
        if not User._flag:
            self.name = ''
            self.table_list = ('_record', '_mark', '_taste', '_nutrition', '_frequency')
            self.record_key = ('canteen', 'counter', 'dish', 'date', 'times', 'ID')
            self.record_type = ('varchar(50) not null', 'varchar(50) not null', 'varchar(50) not null', 'varchar(50) not null',
                                'varchar(20) not null', 'int not null')
            self.mark_key = ('ID', 'name', 'mark')
            self.mark_type = ('int not null', "varchar(50) not null DEFAULT ''",
                              "varchar(100) not null DEFAULT ''")
            self.taste_key = ('麻辣', '清淡', '酸辣', '香辣', '酱香', '甜味', '酸甜', '酸咸', '甜咸', '咸香')
            self.taste_type = ('int not null DEFAULT 0', 'int not null DEFAULT 0', 'int not null DEFAULT 0',
                               'int not null DEFAULT 0', 'int not null DEFAULT 0', 'int not null DEFAULT 0', 'int not null DEFAULT 0',
                               'int not null DEFAULT 0', 'int not null DEFAULT 0', 'int not null DEFAULT 0')
            self.nutrition_key = ('碳水', '肉类', '蔬菜')
            self.nutrition_type = ('int not null DEFAULT 0', 'int not null DEFAULT 0', 'int not null DEFAULT 0')
            self.frequency_key = ('canteen', 'counter', 'name', 'taste', 'nutrition', 'num')
            self.frequency_type = ('varchar(50) not null', 'varchar(50) not null', 'varchar(50) not null', 'varchar(50) not null',
                                'varchar(50) not null', 'int not null DEFAULT 0')
            self.user_key = ('name', 'password')
            User._flag = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def register(self, name, password):
        if len(name) > 6 or len(password) > 12 or len(name) == 0 or check_same('user', 'name', name, 'str'):
            return False
        else:
            value = (name, password)
            db = DB()
            for i in range(len(self.table_list)):
                table_name = name + self.table_list[i]
                if i < 1:
                    db.create_table(table_name, self.record_key, self.record_type)
                elif i == 1:
                    db.create_table(table_name, self.mark_key, self.mark_type)
                elif i == 2:
                    db.create_table(table_name, self.taste_key, self.taste_type)
                elif i == 3:
                    db.create_table(table_name, self.nutrition_key, self.nutrition_type)
                elif i == 4:
                    db.create_table(table_name, self.frequency_key, self.frequency_type)
            db.insert('user', self.user_key, value)
        return True

    def login(self, name, password):
        if len(name) > 6 or len(password) > 12 or len(name) == 0 or not check_same('user', 'name', name, 'str'):
            return False
        db = DB()
        result = db.find_key('user', 'name', name, 'str')
        if result[0][1] == password:
            self.name = name
            return True
        else:
            return False

    def get_table_name(self, table):
        return self.name + self.table_list[table]

    def exit(self):
        self.name = ''
        return

    def change(self, passWord):
        db = DB()
        db.change('user', 'name', self.name, 'password', passWord)

    def destroy(self):
        if len(self.name) > 0:
            db = DB()
            for i in range(5):
                table_name = self.get_table_name(i)
                db.delete_table(table_name)
            db.delete_data('user', 'name', self.name)
            self.exit()
            self._flag = False
