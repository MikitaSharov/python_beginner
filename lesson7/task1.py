from random import randint, uniform


def random_int_float_in_file(path, lines):
    with open(path, 'a', encoding='utf-8') as file:
        for line in range(lines):
            print(f'{randint(-1000, 1001)}|{round(uniform(-1000, 1000), 2)}', file=file)


if __name__ == '__main__':
    random_int_float_in_file('task1.txt', 5)
