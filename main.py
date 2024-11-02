from datetime import datetime
from typing import Dict, List

# Функция для вычисления оценки
def deadline_score(pass_date: str, deadline_date: str) -> int:
    date_format = "%d.%m.%Y"
    try:
        pass_dt = datetime.strptime(pass_date, date_format)
        deadline_dt = datetime.strptime(deadline_date, date_format)
    except ValueError:
        raise ValueError("Некорректный формат даты. Ожидается формат 'DD.MM.YYYY'.")

    if pass_dt <= deadline_dt:
        return 5

    delay_days = (pass_dt - deadline_dt).days
    delay_weeks = delay_days // 7
    score = max(5 - delay_weeks, 0)
    return score

# Функция для списка опоздавших студентов
def late_list():
    pass

# Настройка командной строки

# Основная функция
def main():
    pass

if __name__ == "__main__":
    main()
