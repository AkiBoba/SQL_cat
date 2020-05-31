import pandas as pd
import pymysql

con = pymysql.connect('127.0.0.1', 'root', '1141', 'basic_sql')

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
cat = pd.read_csv('D:\PycharmProjects\Каталог_Олег\pattern.csv')
cat.columns = cat.columns.str.replace(' ', '_')
with con:
    for i in range(len(cat)):
        cur = con.cursor()
        sql = 'insert into primer (insert into mycat(\
            Номер_поставляемой_запчасти,\
            Производитель,\
            Название,\
            Артикул_OEM,\
            замены,\
            Группа,\
            Подкатегория,\
            Применение,\
            Серия,\
            Комментарий_к_детали,\
            Вес,\
            Изображения,\
            URL) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (f'{cat.Номер_поставляемой_запчасти[i]}',
               f'{cat.Производитель[i]}',
               f'{cat.Название[i]}',
               f'{cat.Артикул_OEM[i]}',
               f'{cat.замены[i]}',
               f'{cat.Группа[i]}',
               f'{cat.Подкатегория[i]}',
               f'{cat.Применение[i]}',
               f'{cat.Серия[i]}',
               f'{cat.Комментарий_к_детали[i]}',
               f'{cat.Вес[i]}',
               f'{cat.Изображения[i]}',
               f'{cat.URL[i]}')
        # print(sql, val)
        cur.execute(sql, val)

# print(cat.head(5))
