import pandas as pd

# Загрузка данных из файла Excel
df = pd.read_excel('finishdata.xlsx')
# Создаем переменную, в которую записываем количество строк
num_rows_to_select = 50
# Создаем список, в котором указываем наименование полей
columns_to_select = ['Название вакансии', 'Работодатель', 'Заработная плата']
columns_to_select1 = ['Название вакансии', 'Работодатель', 'Заработная плата', 'Дата публикации','Описание вакансии', 'Ключевые навыки', 'Название региона', 'График работы', 'Опыт работы']


# Выборка указанного количества строк и столбцов
sample_df = df.loc[:num_rows_to_select-0, columns_to_select]
sample_df1 = df.loc[:num_rows_to_select-0, columns_to_select1]

# Вывод выборки на экран
print(sample_df)
print("\n\n\n\n Новая выборка \n\n\n\n\n")
print(sample_df1)
