from datetime import datetime
from typing import Dict, List
import argparse


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
def late_list(grades: Dict[str, str], deadline_date: str) -> List[str]:
    late_students = []

    for student, pass_date in grades.items():
        try:
            if deadline_score(pass_date, deadline_date) < 5:
                late_students.append(student)
        except ValueError:
            print(f"Некорректный формат даты для студента {student}.")

    return sorted(late_students)


# Настройка командной строки
parser = argparse.ArgumentParser(description="Программа для обработки дедлайнов и оценок студентов")
subparsers = parser.add_subparsers(dest="command")

# Основная функция
def main():
    pass

if __name__ == "__main__":
    main()

