from pandas import DataFrame


def get_average_age(data_frame: DataFrame, sex: str) -> int:
    if sex == "Female":
        return round(data_frame[data_frame['sex'] == 'Female']['age'].mean())
    else:
        return round(data_frame[data_frame['sex'] == 'Male']['age'].mean())


def get_german_percentage(data_frame: DataFrame) -> str:
    germans = (data_frame['native-country'] == 'Germany').sum()
    total_entries = len(data_frame)
    return str(round(germans / total_entries * 100, 2)) + "%"


def has_university_degree(education: str) -> bool:
    university_degrees = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']
    return education in university_degrees


def all_high_income_have_university(data_frame: DataFrame) -> bool:
    high_income = data_frame[data_frame['salary'] == '>50K']
    return high_income['education'].apply(has_university_degree).all()


def is_high_income_comes_with_university(data_frame: DataFrame) -> str:
    if all_high_income_have_university(data_frame):
        return "Все люди, зарабатывающее свыше 50 000, имеют высшее образование."
    else:
        return "Найдены люди, не имеющие высшего образования, но зарабатывающие свыше 50 000."


def get_age_statistics_by_race_and_gender(data_frame: DataFrame) -> DataFrame:
    return data_frame.groupby(['race', 'sex'])['age'].describe()['mean']


def max_age_amer_indian_eskimo_male(data_frame: DataFrame) -> int:
    return data_frame[(data_frame['race'] == 'Amer-Indian-Eskimo') & (data_frame['sex'] == 'Male')]['age'].max()


def categorize_marital_status(status: str) -> str:
    if status.startswith('Married'):
        return 'Married'
    else:
        return 'Unmarried'


def proportion_high_earners_by_marital_status(data_frame: DataFrame) -> tuple:
    data_frame['marital_status_category'] = data_frame['marital-status'].apply(categorize_marital_status)
    men = data_frame[data_frame['sex'] == 'Male']
    high_earners = men[men['salary'] == '>50K']
    proportion_married = (high_earners[high_earners['marital_status_category'] == 'Married'].shape[0] /
                          men[men['marital_status_category'] == 'Married'].shape[0])
    proportion_unmarried = (high_earners[high_earners['marital_status_category'] == 'Unmarried'].shape[0] /
                            men[men['marital_status_category'] == 'Unmarried'].shape[0])
    return f"{str(round(proportion_married * 100, 2))}%", f"{str(round(proportion_unmarried * 100, 2))}%"


def compare_proportions(proportion_married: float, proportion_unmarried: float) -> str:
    if proportion_married > proportion_unmarried:
        return "Богатые мужчины — в основном женаты."
    elif proportion_married < proportion_unmarried:
        return "Богатые мужчины — в основном холосты."
    else:
        return "Количество богатых как среди женатых, так и холостых одинаково."


def percentage_a_lot_max_hours_people(dataframe: DataFrame, max_hours_per_week: int, num_people_max_hours: int) -> str:
    high_earners_max_hours = dataframe[(dataframe['hours-per-week'] == max_hours_per_week)
                                       & (dataframe['salary'] == '>50K')].shape[0]
    return f"{round(high_earners_max_hours / num_people_max_hours * 100, 2)}%"
