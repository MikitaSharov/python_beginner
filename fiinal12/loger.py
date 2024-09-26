# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит: имя файла без расширения или название каталога, расширение, если это файл, флаг каталога,
# название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import sys
import logging
from collections import namedtuple


FileInfo = namedtuple('FileInfo', 'name ext is_dir parent_dir')

logging.basicConfig(filename='info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def collect_directory_info(path):
    if not os.path.isdir(path):
        logging.error('неверный путь')
        return []

    collected_info = []

    for entry in os.scandir(path):
        name, ext = os.path.splitext(entry.name)
        is_dir = entry.is_dir()
        parent_dir = os.path.basename(path)

        file_info = FileInfo(name, ext if not is_dir else '', is_dir, parent_dir)
        collected_info.append(file_info)

        logging.info(file_info)

    return collected_info

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('надо py script.py path')
        sys.exit(1)

    path = sys.argv[1]
    info = collect_directory_info(path)

    for item in info:
        print(item)