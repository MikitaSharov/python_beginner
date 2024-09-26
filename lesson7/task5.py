# Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import choice
from task4 import create_file


def create_files(*extensions, qty_files):
    for _ in range(qty_files):
        extension = choice(extensions)
        create_file(extension, qty_files=1)


if __name__ == '__main__':
    create_files('txt', 'mp3', 'doc', 'avi', qty_files=5)
