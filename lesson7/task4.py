# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import choice, randint
from string import ascii_lowercase
from os import urandom


def create_file(extension, min_len_filename=6, max_len_filename=30, min_bytes=256, max_bytes=4096, qty_files=5):
    for _ in range(qty_files):
        name = ''.join(choice(ascii_lowercase) for _ in range(randint(min_len_filename, max_len_filename)))
        filename = f'{name}.{extension}'
        input_bytes = urandom(randint(min_bytes, max_bytes))

        with open(filename, 'wb') as file:
            file.write(input_bytes)


if __name__ == '__main__':
    create_file('txt')
