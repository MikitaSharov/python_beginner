# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from os import makedirs, path, urandom
from random import choice, randint
from string import ascii_lowercase


def create_file(directory, extension, min_len_filename=6, max_len_filename=30, min_bytes=256, max_bytes=4096,
                qty_files=5):
    if not path.exists(directory):
        makedirs(directory)

    while True:
        name_length = randint(min_len_filename, max_len_filename)
        name = ''.join(choice(ascii_lowercase) for _ in range(name_length))
        filename = path.join(directory, f'{name}.{extension}')
        if not path.exists(filename):
            break

    input_bytes = urandom(randint(min_bytes, max_bytes))

    with open(filename, 'wb') as file:
        file.write(input_bytes)


def create_files(*extensions, directory='.', qty_files):
    for _ in range(qty_files):
        extension = choice(extensions)
        create_file(directory, extension, qty_files=1)


create_files('txt', 'mp3', 'doc', 'avi', directory='created_files', qty_files=5)
