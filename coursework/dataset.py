import pandas as pd
from pandas import DataFrame
from tabulate import tabulate
from dataset_console import Message
from visualisation import Visualisation


class Dataset:
    def __init__(self):
        """
        Конструктор класса Dataset
        """
        try:
            self.data: DataFrame = pd.read_csv('Student Mental health.csv')
            Message('info', 'Файл "Student Mental health.csv" успешно загружен')
        except FileNotFoundError:
            Message('error', 'Файл "Student Mental health.csv" не найден')
            return
        except ValueError:
            Message('warning', 'Указан неверный тип консольного сообщения')

        Message('info', 'Начинаем предобработку данных.')
        try:
            self.preprocessing = Preprocessing(self.data)
            self.preprocessing.preprocess()
            Message('info', 'Предобработка данных завершена.')
        except Exception as e:
            Message('error', f'Произошла ошибка при предобработке данных: {e}')

        Message('info', 'Подготовка к визуализации данных...')
        visualise = Visualisation(self.data)
        Message('info', 'Подготовка завершена.')

        Message('info', 'Запуск визуализации данных...')
        visualise.age_distribution()
        visualise.age_distribution_among_different_academic_years()
        visualise.gender_distribution()
        visualise.marital_status_distribution()
        visualise.marital_status_cgpa_impact()
        visualise.depression_distribution()
        visualise.marital_status_depression_impact()
        visualise.cgpa_panic_attacks_correlation()
        visualise.cgpa_depression_correlation()


class Preprocessing:
    def __init__(self, data: DataFrame):
        self.data = data

    def check_for_duplicates(self) -> bool:
        """
        Процедура проверки на наличие дубликатов
        :return:
        """
        return self.data.duplicated().any()

    def preprocess(self):
        """
        Процедура предобработки данных:
        1. Изменение названий столбцов
        2. Удаление ненужных столбцов
        3. Удаление позиций с пустыми значениями
        4. Удаление дубликатов
        5. Приведение столбцов к нужным типам данных для облегчения дальнейшего анализа
        :return:
        """
        try:
            Message('info', 'Шаг 1: Изменить названия столбцов для более лаконичного вида.')
            self.change_headers_names()
        except Exception as e:
            Message('error', f'Произошла ошибка при изменении названий столбцов: {e}')
            return
        try:
            Message('info', 'Шаг 2: Удалить ненужные столбцы.')
            self.remove_unnecessary_columns()
        except Exception as e:
            Message('error', f'Произошла ошибка при удалении ненужных столбцов: {e}')
            return
        try:
            Message('info', 'Шаг 3: Удалить позиции с пустыми значениями.')
            self.data.dropna(inplace=True)
        except Exception as e:
            Message('error', f'Произошла ошибка при удалении позиций с пустыми значениями: {e}')
            return
        try:
            Message('info', 'Шаг 4: Удалить дубликаты.')
            self.data.drop_duplicates(inplace=True)
        except Exception as e:
            Message('error', f'Произошла ошибка при удалении дубликатов: {e}')
            return
        try:
            Message('info', 'Шаг 5: Привести столбцы к нужным типам данных для облегчения дальнейшего анализа.')
            self.changing_types()
        except Exception as e:
            Message('error', f'Произошла ошибка при приведении столбцов к нужным типам данных: {e}')
            return

    def change_headers_names(self):
        """
        Функция изменения названий столбцов для более лаконичного вида
        :return:
        """
        _ = {
            'Timestamp': 'Date',
            'Choose your gender': 'Gender',
            'Age': 'Age',
            'What is your course?': 'Major',
            'Your current year of Study': 'Year of Study',
            'What is your CGPA?': 'CGPA',
            'Do you have Depression?': 'Depression',
            'Do you have Anxiety?': 'Anxiety',
            'Do you have Panic attack?': 'Panic Attacks',
            'Did you seek any specialist for a treatment?': 'Treatment from a Specialist'
        }

        self.data.rename(columns=_, inplace=True)

    def remove_unnecessary_columns(self):
        """
        Убираем столбцы, в которых нет необходимости в контексте текущего анализа
        :return:
        """
        self.data.drop(columns=['Date'], axis=1)

    def changing_types(self):
        """
        Приведение столбцов к нужным типам данных для облегчения дальнейшего анализа
        :return:
        """
        self.data['Age'] = self.data['Age'].astype('int')
        self.data['Year of Study'] = self.data['Year of Study'].astype('str').apply(self.convert_years_of_study).astype(
            'int')
        self.data['CGPA'] = self.data['CGPA'].astype('str')
        self.data['CGPA'] = self.data['CGPA'].apply(self.convert_gpa).astype(float)

    @staticmethod
    def convert_gpa(value: str) -> float:
        """
        Усредняем диапазон GPA путём нахождения среднего значения
        :param value:
        :return:
        """
        if '-' in value:
            start, end = map(float, value.split(' - '))
            return round((start + end) / 2, 2)
        else:
            return round(float(value), 2)

    @staticmethod
    def convert_years_of_study(value: str) -> int:
        """
        Преобразование курса в числовой формат
        Изначальный формат: "Year 1", "Year 2", ..., "Year 5" (регистр не учитывается)
        Формат на выходе: 1, 2, ..., 5
        :param value:
        :return:
        """
        return int(value[-1])

    def get_majors(self):
        """
        Получаем список всех специальностей
        :return:
        """
        return self.data['Major'].unique()

    def get_years_of_study(self):
        """
        Получаем список всех курсов
        :return:
        """
        return self.data['Year of Study'].unique()


class Display:
    def __init__(self, data: DataFrame):
        self.data = data

    def display(self, headers_only: bool = False):
        """
        Use tabulate to display neat table
        """
        if not headers_only:
            print(tabulate(self.data, headers='keys', tablefmt='pretty'))
        else:
            print(tabulate(self.data.head(0), headers='keys', tablefmt='pretty'))
