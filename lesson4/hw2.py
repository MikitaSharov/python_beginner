# апишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
#
# Пример использования.
# На входе:
#
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# На выходе:
#
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

def key_params(**kwargs):
    input_params = dict(*locals().values())
    result = {}

    for key, value in input_params.items():
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key

    return result

print(key_params(a=1, b='hello', c=[1, 2, 3], d={}))