# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
#
# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
#
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')

def get_file_info(file_path):
    *left_part, file_name = [part for part in file_path.split('/')]
    *file_name, extension = [part for part in file_name.split('.')]

    directory = ''
    for part in left_part:
        directory += part + '/'

    name = '.'.join(file_name)

    return (directory, name, f'.{extension}')


file_path = "C:/Users/User/Documents/example.txt"

print(get_file_info(file_path))
# print(get_file_info(file_path))
