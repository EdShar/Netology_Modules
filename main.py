from os import path
from datetime import datetime
from application.salary import calculate_salary as salary
from application.db.people import get_employees as employees


def today():
    print(f'Сегодня: {datetime.now().date()}')


if __name__ == '__main__':
    print(f'Имя исполняемого файла: {path.basename(__file__)}')
    today()
    employees()
    salary()
