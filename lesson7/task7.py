#  Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil

# Определяем расширения для каждой категории
CATEGORIES = {
    'videos': ['mp4', 'mkv', 'avi', 'mov', 'flv'],
    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
    'text': ['txt', 'doc', 'docx', 'pdf', 'md'],
    'audio': ['mp3', 'wav', 'aac', 'flac']
}


def sort_files(base_directory):
    """
    Сортирует файлы в указанной директории и всех её поддиректориях по категориям в подкаталоги.
    Оставляет файлы, которые не подошли ни под одну категорию, в исходной директории.

    :param base_directory: Путь к исходной директории.
    """
    if not os.path.exists(base_directory):
        print(f"Директория {base_directory} не существует.")
        return

    # Создаем подкаталоги для каждой категории в основной директории
    for category in CATEGORIES:
        category_path = os.path.join(base_directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Используем os.walk для обхода всех директорий
    for dirpath, _, filenames in os.walk(base_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Получаем расширение файла
            _, ext = os.path.splitext(filename)
            ext = ext.lstrip('.').lower()

            # Определяем категорию файла
            moved = False
            for category, extensions in CATEGORIES.items():
                if ext in extensions:
                    dest_path = os.path.join(base_directory, category, filename)
                    shutil.move(file_path, dest_path)
                    moved = True
                    break

            # Если файл не подошел ни под одну категорию, оставляем его в исходной директории
            if not moved:
                print(f"Файл '{filename}' не подошел ни под одну категорию и остался в исходной директории.")

        # Удаляем пустые поддиректории после перемещения файлов
        if dirpath != base_directory:  # Не удаляем корневую директорию
            if not os.listdir(dirpath):  # Проверяем, пуст ли каталог
                os.rmdir(dirpath)
                print(f"Удалена пустая директория: {dirpath}")


if __name__ == '__main__':
    sort_files('./created_files')
