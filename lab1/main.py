from helper import *

data_frame = pd.read_csv('adult.csv')  # Чтение файла adult.csv
number = data_frame.count().iloc[0]  # Получение числа позиций в DataFrame
types = get_data_types(data_frame)  # Получение типа данных каждого столбца в DataFrame
quantitative = get_int64_columns(data_frame)
qualitative = get_non_int64_columns(data_frame)

average_age = round(get_average_value(data_frame, "age"))
maximum_age = round(get_max_value(data_frame, "age"))
minimum_age = round(get_min_value(data_frame, "age"))

average_fnlwgt = round(get_average_value(data_frame, "fnlwgt"))
maximum_fnlwgt = round(get_max_value(data_frame, "fnlwgt"))
minimum_fnlwgt = round(get_min_value(data_frame, "fnlwgt"))

average_educational_num = round(get_average_value(data_frame, "educational-num"))
maximum_educational_num = round(get_max_value(data_frame, "educational-num"))
minimum_educational_num = round(get_min_value(data_frame, "educational-num"))

average_capital_gain = round(get_average_value(data_frame, "capital-gain"))
minimum_capital_gain = round(get_min_value(data_frame, "capital-gain"))
maximum_capital_gain = round(get_max_value(data_frame, "capital-gain"))

average_capital_loss = round(get_average_value(data_frame, "capital-loss"))
minimum_capital_loss = round(get_min_value(data_frame, "capital-loss"))
maximum_capital_loss = round(get_max_value(data_frame, "capital-loss"))

average_hours_per_week = round(get_average_value(data_frame, "hours-per-week"))
minimum_hours_per_week = round(get_min_value(data_frame, "hours-per-week"))
maximum_hours_per_week = round(get_max_value(data_frame, "hours-per-week"))

widowed_frequency = data_frame['marital-status'].value_counts()['Widowed']
male_frequency = data_frame['gender'].value_counts()['Male']
female_frequency = data_frame['gender'].value_counts()['Female']

null_count = get_null_cells_number(data_frame)
uncompleted_objects_number = get_uncompleted_objects_number(data_frame)

print("Лабораторная работа №1. Автор: Петрушов Дмитрий Владимирович")
print()
print("Название считываемого файла: adult.csv")
print("Число позиций:", number)
print("Типы данных:")
print(types)
print()
print("Количественные характеристики:", quantitative)
print("Качественные характеристики:", qualitative)
print()
print("Максимальный возраст:", maximum_age)
print("Среднестатистический возраст:", average_age)
print("Минимальный возраст:", minimum_age)
print()
print("Максимальный показатель fnlwgt:", maximum_fnlwgt)
print("Среднестатистический показатель fnlwgt:", average_fnlwgt)
print("Минимальный показатель fnlwgt:", minimum_fnlwgt)
print()
print("Максимальный показатель fnlwgt:", maximum_fnlwgt)
print("Среднестатистический показатель fnlwgt:", average_fnlwgt)
print("Минимальный показатель fnlwgt:", minimum_fnlwgt)
print()
print("Максимальный показатель education-num:", maximum_educational_num)
print("Среднестатистический показатель education-num:", average_educational_num)
print("Минимальный показатель education-num:", minimum_educational_num)
print()
print("Максимальный показатель прироста капитала:", maximum_capital_gain)
print("Среднестатистический показатель прироста капитала:", average_capital_gain)
print("Минимальный показатель прироста капитала:", minimum_capital_gain)
print()
print("Максимальный показатель потери капитала:", maximum_capital_loss)
print("Среднестатистический показатель потери капитала:", average_capital_loss)
print("Минимальный показатель потери капитала:", minimum_capital_loss)
print()
print("Максимальное количество рабочих часов в неделю:", maximum_capital_loss)
print("Среднее количество рабочих часов в неделю:", average_capital_loss)
print("Минимальное количество рабочих часов в неделю:", minimum_capital_loss)
print()
print("Частота встречаемости вдовцов и вдов суммарно:", widowed_frequency)
print("Количество женщин:", female_frequency)
print("Количество мужчин:", male_frequency)

print("Количество ячеек с отсутствующими данными", null_count)
print("Количество объектов с неполной информацией:", uncompleted_objects_number)

plot_age_distribution(data_frame)
plot_widowed_comparison(data_frame)
plot_age_distribution_widowed(data_frame)
