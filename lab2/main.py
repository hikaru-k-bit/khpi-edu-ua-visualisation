import pandas as pd

import helper
from helper import *

data_frame = pd.read_csv('adult.data.csv')  # Чтение файла adult.csv
number = data_frame.count().iloc[0]
male_frequency = data_frame['sex'].value_counts()['Male']
female_frequency = data_frame['sex'].value_counts()['Female']
avg_woman_age = get_average_age(data_frame, 'Female')
avg_man_age = get_average_age(data_frame, 'Male')
german_percentage = get_german_percentage(data_frame)
high_income_mean_age = round(data_frame[data_frame['salary'] == '>50K']['age'].mean())
high_income_std_age = data_frame[data_frame['salary'] == '>50K']['age'].std()
low_income_mean_age = data_frame[data_frame['salary'] == '<=50K']['age'].mean()
low_income_std_age = data_frame[data_frame['salary'] == '<=50K']['age'].std()
age_stats = get_age_statistics_by_race_and_gender(data_frame)
max_age_indian_eskimo_male = max_age_amer_indian_eskimo_male(data_frame)
proportion_married, proportion_unmarried = proportion_high_earners_by_marital_status(data_frame)
max_hours_per_week = data_frame['hours-per-week'].max()
num_people_max_hours = data_frame[data_frame['hours-per-week'] == max_hours_per_week].shape[0]
average_hours_worked_by_salary_and_country = data_frame.groupby(['native-country', 'salary'])['hours-per-week'].mean()

print("Лабораторная работа №1. Автор: Петрушов Дмитрий Владимирович")
print()
print("Название считываемого файла: adult.data.csv")
print("Число позиций:", number)
print("Количество женщин:", female_frequency)
print("Количество мужчин:", male_frequency)
print("Средний возраст женщин:", avg_woman_age)
print("Средний возраст мужчин:", avg_man_age)
print("Процент граждан Германии:", german_percentage)
print("Средний возраст людей с высоким уровнем дохода:", high_income_mean_age)
print("Среднеквадратичное отклонение для людей с высоким уровнем дохода:", high_income_std_age)
print("Средний возраст людей с низким уровнем дохода:", low_income_mean_age)
print("Среднеквадратичное отклонение для людей с низким уровнем дохода:", low_income_std_age)
print()
print(helper.is_high_income_comes_with_university(data_frame))
print()
print("Статистика возраста для каждого пола и расы:")
print()
print(age_stats)
print()
print("Максимальный возраст среди индейцев-эскимосов мужского пола:", max_age_indian_eskimo_male)
print()
print("Доля богатых среди женатых мужчин:", proportion_married)
print("Доля богатых среди неженатых мужчин:", proportion_unmarried)
print(compare_proportions(proportion_married, proportion_unmarried))
print()
print("Максимальное число рабочих часов в неделю:", max_hours_per_week)
print(f"Количество людей, которые работают {max_hours_per_week} часов: {num_people_max_hours}")
print("Из них много зарабатывают:",
      percentage_a_lot_max_hours_people(data_frame, max_hours_per_week, num_people_max_hours))
print()
print(average_hours_worked_by_salary_and_country)
