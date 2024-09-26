# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
#
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.
#
# Пример использования На входе:
#
#
# date_to_prove = 15.4.2023
# На выходе:
# True
#
# На входе:
import datetime

date_to_prove = 31.6.2022


def date(date_to_prove: str) -> bool:
    day, month, year = map(int, date_to_prove.split('.'))
    days_in_month = {(1, 3, 5, 7, 8, 10, 12): 31, (4, 6, 9, 11): 30, (2,): 28}

    if year < 0:
        return False

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        days_in_month[(2,)] = 29

    for months, days in days_in_month.items():
        if month in months and day in range(1, days + 1):
            return True
    return False


date_to_prove = '28.2.2023'
print(date(date_to_prove))
