# Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл

from random import randint, choice
from string import ascii_lowercase


def random_nickname():
    while True:
        nickname = ''.join(choice(ascii_lowercase) for _ in range(randint(4, 7)))

        nickname = nickname[0].upper() + nickname[1:]  # .capitalize()

        for char in nickname:  # if any(char in 'aeiouAEIOU' for char in nickname)
            if char in 'aeiouAEIOU':
                return nickname


def random_nickname_in_file(path, lines):
    with open(path, 'a', encoding='utf-8') as file:
        for _ in range(lines):
            print(f'{random_nickname()}', file=file)


random_nickname_in_file('task2.txt', 3)
