import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
df = pd.read_excel('488446--gwindustrial.ru.xls',
                   sheet_name='общая')  # все колонки загружены из таблицы, страница "общая"
# df[]
# print(df.head(2))
cat_df = pd.DataFrame({'Номер поставляемой запчасти': df.Артикул, 'Производитель': df.Бренд,
                       'Название': df.Название, 'Артикул OEM': df.Артикул, 'замены': df.Замена, 'Группа': df.Группа,
                       'Подкатегория': df.Подкатегория, 'Применение': df.Применение, 'Серия': df.Серия,
                       'Комментарий к детали': df['Комментарий к детали'], 'Вес': df.Вес, 'Изображения': df.Изображения,
                       'URL': df['URL']
                       })


for i in range(len(cat_df)):
    cat_df['Номер поставляемой запчасти'][i] = ''.join(cat_df['Номер поставляемой запчасти'][i].split()[0])
    cat_df.Название[i] = ' '.join(cat_df.Название[i].split()[2:])
    cat_df.замены[i] = '; '.join(str(cat_df.замены[i]).split())
writer = pd.ExcelWriter('pattern.xls', engine='xlsxwriter')  # запись полученной таблицы в файл
# Write your DataFrame to a file
cat_df.to_excel(writer, 'cat')  # запись полученной таблицы в файл
# Save the result
writer.save()  # запись полученной таблицы в файл

cat_df.to_csv('pattern.csv', index=False)
