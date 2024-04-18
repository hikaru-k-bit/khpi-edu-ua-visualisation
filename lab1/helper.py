from typing import List, Optional

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tabulate import tabulate


def get_data_types(data_frame: pd.DataFrame) -> str:
    types = data_frame.dtypes
    headers = ["Column Name", "Data Type"]
    rows = [(column_name, str(data_type)) for column_name, data_type in types.items()]
    return tabulate(rows, headers=headers, tablefmt="fancy_grid")


def get_int64_columns(data_frame: pd.DataFrame) -> List:
    int64_columns = [column for column, dtype in data_frame.dtypes.items() if dtype == "int64"]
    return int64_columns


def get_non_int64_columns(data_frame: pd.DataFrame) -> List:
    non_int64_columns = [column for column, dtype in data_frame.dtypes.items() if dtype != "int64"]
    return non_int64_columns


def get_average_value(data_frame: pd.DataFrame, column_name: str) -> Optional[float]:
    if column_name in data_frame.columns:
        average_age = data_frame[column_name].mean()
        return average_age
    else:
        return None


def get_max_value(data_frame: pd.DataFrame, column_name: str) -> Optional[int]:
    if column_name in data_frame.columns:
        max_age = data_frame[column_name].max()
        return max_age
    else:
        return None


def get_min_value(data_frame: pd.DataFrame, column_name: str) -> Optional[int]:
    if column_name in data_frame.columns:
        max_age = data_frame[column_name].min()
        return max_age
    else:
        return None


def get_null_cells_number(data_frame: pd.DataFrame) -> int:
    question_marks_count = 0
    for column in data_frame.columns:
        question_marks_count += (data_frame[column] == '?').sum()
    return question_marks_count


def get_uncompleted_objects_number(data_frame: pd.DataFrame) -> int:
    rows_with_question_marks = (data_frame == '?').any(axis=1)
    return rows_with_question_marks.sum()


def plot_age_distribution(data_frame: pd.DataFrame) -> None:
    male_data = data_frame[data_frame['gender'] == 'Male']
    female_data = data_frame[data_frame['gender'] == 'Female']

    plt.figure(figsize=(10, 6))
    plt.hist(male_data['age'], bins=20, color='blue', alpha=0.5, label='Мужчины')
    plt.hist(female_data['age'], bins=20, color='pink', alpha=0.5, label='Женщины')
    plt.title('Распределение возраста по полу')
    plt.xlabel('Возраст')
    plt.ylabel('Количество')
    plt.legend()
    plt.grid(axis='y')
    plt.show()


def plot_widowed_comparison(data_frame: pd.DataFrame) -> None:
    widowed_counts = data_frame[data_frame['marital-status'] == 'Widowed']['gender'].value_counts()

    plt.figure(figsize=(8, 6))
    widowed_counts.plot(kind='bar', color=['blue', 'pink'])

    plt.title('Количество вдов и вдовцов')
    plt.xlabel('Пол')
    plt.ylabel('Количество')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.show()


def plot_age_distribution_widowed(data_frame: pd.DataFrame) -> None:
    widowed_data = data_frame[data_frame['marital-status'] == 'Widowed']

    plt.figure(figsize=(10, 6))
    sns.violinplot(x='gender', y='age', data=widowed_data, hue='gender', palette={"Male": "blue", "Female": "pink"},
                   legend=False)

    plt.title('Статистика овдовевших по возрасту и полу')
    plt.xlabel('Пол')
    plt.ylabel('Возраст')
    plt.grid(axis='y')
    plt.xticks(ticks=[0, 1], labels=['Женщины', 'Мужчины'])
    plt.show()
