import pandas as pd

# Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить
# представление о структуре данных.
# Выведите информацию о данных (.info())
# и статистическое описание (.describe()).

df = pd.read_csv('Most Popular Programming Languages.csv')
# Выводим информацию о данных
print('Первые 5 строк данных:')
print(df.head(5), end='\n\n')

print('Информация о данных (.info()):')
df.info()
print()

print('Статистическое описание (.describe()):')
print(df.describe())
print()

# Определите среднюю зарплату (Salary)
# по городу (City) - используйте файл приложенный к дз - dz.csv
print('Информация из файла dz.csv:')
df = pd.read_csv('dz.csv')
print(df)
print()

print('Средняя зарплата по городу:')
# Определение средней зарплаты по городу
average_salary_by_city = df.groupby('City')['Salary'].mean().reset_index()

# Печать результата
print(average_salary_by_city)