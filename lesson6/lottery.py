# Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from random import randint
import sys


def guess(start, finish, max_try):
    hidden_number = randint(start, finish + 1)

    for _ in range(max_try):
        player_number = int(input(f'Введите число от {start} до {finish}: '))

        if player_number < hidden_number:
            print('Загаданное число больше')
        elif player_number > hidden_number:
            print('Загаданное число меньше')
        else:
            return True

    return False


if __name__ == '__main__':
    start = 1
    finish = 10
    max_try = 5

    args = sys.argv[1:4]

    if len(args) >= 1:
        start = int(args[0])
    if len(args) >= 2:
        finish = int(args[1])
    if len(args) >= 3:
        max_try = int(args[2])
    print(guess(start, finish, max_try))
