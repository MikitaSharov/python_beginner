# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from math import prod


def func3():
    with (
        open('task1.txt', 'r', encoding='utf-8') as f1,
        open('task2.txt', 'r', encoding='utf-8') as f2,
        open('task3.txt', 'w', encoding='utf-8') as f3
    ):
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()
        max_lines = max(len(f1_lines), len(f2_lines))

        f1_lines = f1_lines * (max_lines // len(f1_lines)) + f1_lines[:max_lines % len(f1_lines)]
        f2_lines = f2_lines * (max_lines // len(f2_lines)) + f2_lines[:max_lines % len(f2_lines)]

        for numbers_line, name_line in zip(f1_lines, f2_lines):
            numbers = list(map(float, numbers_line.strip().split('|')))
            multiple = prod(numbers)
            name = name_line.strip()

            if multiple < 0:
                result_line = f'{name.upper()} | {abs(multiple):.2f}'
            else:
                result_line = f'{name.lower()} | {int(multiple)}'

            print(result_line, file=f3)


func3()
