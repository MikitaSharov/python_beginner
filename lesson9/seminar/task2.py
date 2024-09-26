# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint


def validate_input(func):
    def wrapper(num, attempts):
        if not 1 <= num <= 100:
            num = randint(1, 100)

        if not 1 <= attempts <= 10:
            attempts = randint(1, 10)

        return func(num, attempts)

    return wrapper


@validate_input
def game(num, attempts):
    print(f'угадайте загаданное число {num} за {attempts} попыток')


game(140, 70)
