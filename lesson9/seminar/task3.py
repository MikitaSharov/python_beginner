# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json


def save_to_json(func):
    data = []

    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        result = func(*args, **kwargs)

        my_dict = {'args': args, 'kwargs': kwargs, 'result': result}
        data.append(my_dict)

        with open(file_name, 'a', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

        return result

    return wrapper


@save_to_json
def summa(a, b=2):
    return a + b


summa(2, 3)
summa(5)
summa(10, b=4)
