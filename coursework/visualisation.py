import os

import matplotlib.pyplot as plt
import seaborn as sns

from dataset_console import Message


class Visualisation:
    def __init__(self, data):
        self.data = data

    def age_distribution(self) -> None:
        """
        Процедура построения гистограммы распределения возраста
        :return:
        """
        Message('info', 'Строим гистограмму распределения возраста...')
        plot = sns.histplot(self.data['Age'], kde=True, color='skyblue')
        plt.title('Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Count')

        if not os.path.exists('plots'):
            self.plots_create()
            self.save_plot(plot, 'age_distribution')
        else:
            Message('info', 'Папка plots найдена, сохраняем гистограмму...')
            self.save_plot(plot, 'age_distribution')
        plt.clf()

    def age_distribution_among_different_academic_years(self) -> None:
        """
        Процедура построения гистограммы распределения возраста среди разных курсов
        :return:
        """
        Message('info', 'Строим гистограмму распределения возраста среди разных курсов...')
        plot = sns.countplot(x='Age', hue='Year of Study', data=self.data, palette='pastel')
        plt.title('Year of Study')
        plt.xlabel('Age')
        plt.ylabel('Year of Study')

        if not os.path.exists('plots'):
            self.plots_create()
            self.save_plot(plot, 'age_distribution_among_different_academic_years')
        else:
            Message('info', 'Папка plots найдена, сохраняем гистограмму...')
            self.save_plot(plot, 'age_distribution_among_different_academic_years')
        plt.clf()

    def gender_distribution(self) -> None:
        """
        Процедура построения диаграммы распределения пола
        :return:
        """
        Message('info', 'Строим диаграмму распределения пола...')
        plot = self.data.Gender.value_counts().plot(kind='pie', autopct='%1.1f%%',
                                                    colors=['#ff9999', '#66b3ff', '#99ff99'])
        plt.title('Gender Distribution')

        if not os.path.exists('plots'):
            self.plots_create()
            self.save_plot(plot, 'gender_distribution')
        else:
            Message('info', 'Папка plots найдена, сохраняем диаграмму...')
            self.save_plot(plot, 'gender_distribution')
        plt.clf()

    def marital_status_distribution(self) -> None:
        """
        Процедура построения диаграммы распределения семейного положения
        :return:
        """
        Message('info', 'Строим диаграмму распределения семейного положения...')
        self.data['Marital status'].value_counts().plot(kind='pie', autopct='%1.1f%%',
                                                        colors=['#ff9999', '#66b3ff', '#99ff99'])
        circle = plt.Circle((0, 0), 0.4, color='white')
        plot = plt.gcf().gca().add_artist(circle)
        plt.title('Marital Status')

        if not os.path.exists('plots'):
            self.plots_create()
            self.save_plot(plot, 'marital_status_distribution')
        else:
            Message('info', 'Папка plots найдена, сохраняем диаграмму...')
            self.save_plot(plot, 'marital_status_distribution')
        plt.clf()

    def marital_status_cgpa_impact(self) -> None:
        """
        Процедура построения диаграммы влияния семейного положения на годовую оценку
        :return:
        """
        Message('info', 'Строим диаграмму влияния семейного положения на годовую оценку...')
        plot = sns.violinplot(x='Marital status', y='CGPA', data=self.data, palette='Set2', hue='Marital status',
                              legend=False)
        plt.title('Marital Status vs. CGPA')
        plt.xlabel('Marital Status')
        plt.ylabel('CGPA')

        if not os.path.exists('plots'):
            self.plots_create()
            self.save_plot(plot, 'marital_status_cgpa_impact')
        else:
            Message('info', 'Папка plots найдена, сохраняем диаграмму...')
            self.save_plot(plot, 'marital_status_cgpa_impact')
        plt.clf()

    def depression_distribution(self) -> None:
        """
        Процедура построения диаграммы распределения депрессии
        :return:
        """
        Message('info', 'Строим диаграмму распределения депрессии...')
        fig, ax = plt.subplots()

        pie_data = self.data['Depression'].value_counts()
        colors = ['#ff9999', '#66b3ff']  # pink and blue colors
        labels = ['Fine', 'Depressed']  # Labels for the legend
        ax.pie(pie_data, autopct='%1.1f%%', colors=colors, labels=labels)

        plt.title('Depression Status')

        if not os.path.exists('plots'):
            self.plots_create()
            self.save_plot(fig, 'depression_distribution')
        else:
            Message('info', 'Папка plots найдена, сохраняем диаграмму...')
            self.save_plot(fig, 'depression_distribution')
        plt.clf()

    def marital_status_depression_impact(self) -> None:
        """
        Процедура построения диаграммы влияния семейного положения на депрессию
        :return:
        """
        Message('info', 'Строим диаграмму влияния семейного положения на депрессию...')
        df_depression = self.data[self.data['Depression'] == 'Yes']
        plot = sns.countplot(x='Marital status', hue='Depression', data=df_depression, palette='pastel')
        plt.title('Marital Status vs. Depression')
        plt.xlabel('Marital Status')
        plt.ylabel('Count')

        if not os.path.exists('plots'):
            self.plots_create()
            self.save_plot(plot, 'marital_status_depression_impact')
        else:
            Message('info', 'Папка plots найдена, сохраняем диаграмму...')
            self.save_plot(plot, 'marital_status_depression_impact')
        plt.clf()

    def cgpa_panic_attacks_correlation(self) -> None:
        """
        Процедура построения гистограммы корреляции между CGPA и паническими атаками
        :return:
        """
        Message('info', 'Строим гистограмму корреляции между CGPA и паническими атаками...')
        df_depression = self.data[self.data['Depression'] == 'Yes']
        plot = sns.displot(data=df_depression, x='CGPA', hue='Panic Attacks', palette='Set2', kind='kde', fill=True)
        plt.title('Correlation between CGPA and Panic Attacks')

        if not os.path.exists('plots'):
            self.plots_create()
            self.save_plot(plot, 'cgpa_panic_attacks_correlation')
        else:
            Message('info', 'Папка plots найдена, сохраняем гистограмму...')
            self.save_plot(plot, 'cgpa_panic_attacks_correlation')
        plt.clf()

    def cgpa_depression_correlation(self) -> None:
        """
        Процедура построения гистограммы корреляции между CGPA и депрессией
        :return:
        """
        Message('info', 'Строим гистограмму корреляции между CGPA и депрессией...')
        df_depression = self.data[self.data['Depression'] == 'Yes']
        plot = sns.countplot(x='CGPA', hue='Depression', data=df_depression, palette='Set2')
        plt.title('CGPA vs. Depression')
        plt.xlabel('CGPA')
        plt.ylabel('Count')

        if not os.path.exists('plots'):
            self.plots_create()
            self.save_plot(plot, 'cgpa_depression_correlation')
        else:
            Message('info', 'Папка plots найдена, сохраняем гистограмму...')
            self.save_plot(plot, 'cgpa_depression_correlation')
        plt.clf()

    @staticmethod
    def save_plot(plot: plt.Axes or tuple, filename: str) -> None:
        """
        Процедура сохранения гистограммы
        :param plot:
        :param filename:
        :return:
        """
        try:
            if os.path.exists(f'plots/{filename}.png'):
                Message('io', f'Файл plots/{filename}.png уже существует, перезаписываем...')
            plot.figure.savefig(f'plots/{filename}.png')
            Message('io', f'Гистограмма успешно сохранена по пути plots/{filename}.png')
        except Exception as e:
            Message('error', f'Ошибка при сохранении гистограммы: {e}')

    @staticmethod
    def plots_create() -> None:
        """
        Процедура создания папки plots
        :return:
        """
        Message('io', 'Папка plots не найдена, создаём...')
        try:
            os.makedirs('plots')
            Message('io', 'Папка plots успешно создана')
        except Exception as e:
            Message('error', f'Ошибка при создании папки plots: {e}')