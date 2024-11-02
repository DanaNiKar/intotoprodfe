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

# Подкоманда 'add'
add_parser = subparsers.add_parser("add", help="Добавить дедлайн и список студентов.")
add_parser.add_argument("--deadline", required=True, help="Дата дедлайна в формате DD.MM.YYYY")
add_parser.add_argument("--students", nargs="+", required=True,
                        help="Список студентов и дат сдачи: 'Фамилия=дата'. Пример: Иванов=10.10.2023 Петров=11.10.2023")

# Подкоманда 'late-list'
late_list_parser = subparsers.add_parser("late-list", help="Показать список студентов, сдавших работу позже дедлайна.")
late_list_parser.add_argument("--deadline", required=True, help="Дата дедлайна в формате DD.MM.YYYY")
late_list_parser.add_argument("--students", nargs="+", required=True,
                              help="Список студентов и дат сдачи: 'Фамилия=дата'. Пример: Иванов=10.10.2023 Петров=11.10.2023")

# Подкоманда 'score'
score_parser = subparsers.add_parser("score", help="Узнать оценку студента за работу.")
score_parser.add_argument("--deadline", required=True, help="Дата дедлайна в формате DD.MM.YYYY")
score_parser.add_argument("--student", required=True, help="Фамилия студента, для которого требуется узнать оценку.")
score_parser.add_argument("--pass_date", required=True, help="Дата сдачи работы данного студента в формате DD.MM.YYYY")

# Основная функция
def main():
    while True:
        user_input = input("Введите команду (или 'exit' для завершение): ").strip()

        # Завершение программы по команде 'exit'
        if user_input.lower() == 'exit':
            print("Программа завершена")
            break

        # Разделение команды на аргументы
        args = user_input.split()

        try:
            # Парсинг аргументов
            parsed_args = parser.parse_args(args)

            if parsed_args.command == "add":
                grades = {}
                for student_entry in parsed_args.students:
                    try:
                        student, pass_date = student_entry.split("=")
                        grades[student.strip()] = pass_date.strip()
                    except ValueError:
                        print(f"Ошибка: некорректный формат ввода для '{student_entry}'."
                              f"Ожитается 'Фамилия=дата'")
                        continue

                print("Данные успешно сохранены. Для анализа используйте команду 'late-list' или 'score'.")

            elif parsed_args.command == "late-list":
                grades = {}
                for student_entry in parsed_args.students:
                    try:
                        student, pass_date = student_entry.split("=")
                        grades[student.strip()] = pass_date.strip()
                    except ValueError:
                        print(f"Ошибка: некорректный формат ввода для '{student_entry}'. Ожидается 'Фамилия=дата'.")
                        continue

                late_students = late_list(grades, parsed_args.deadline)
                if late_students:
                    print("Список студентов, сдавших работу позже:")
                    print("/n".join(late_students))
                else:
                    print("Все студенты сдали работу вовремя")

            elif parsed_args.command == "score":
                try:
                    score = deadline_score(parsed_args.pass_date, parsed_args.deadlint)
                    print(f"Оценка для студента {parsed_args.student}: {score}")
                except ValueError as e:
                    print(f"Ошибка: {e}")

            else:
                print("Неизвестная команда. Попробуйте снова")

        except SystemExit:
            # Обработка завершения работы парсера аргументов, если команда некорректна
            print("Ошибка в вводе команды или аргументов. Проверьте ввод и попробуйте снова")

if __name__ == "__main__":
    main()

