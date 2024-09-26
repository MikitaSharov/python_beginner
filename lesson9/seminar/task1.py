# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

def game():
    num = int(input('Загадайте число 1 - 100: '))
    attempts = int(input('Введите кол-во попыток 1 - 10: '))

    def request():
        print(f'угадайте загаданное число за {attempts} попыток')

    return request()


game()
