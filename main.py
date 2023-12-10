from application.salary import calculate_salary
from application.db.people import get_employees
import datetime


def show_today():
    today = datetime.date.today()
    print(today)


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    show_today()
