# Напишите скрипт, который принимает два аргумента командной строки: число и строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать, сколько раз повторить строку в выводе.

import argparse


def main():
    parser = argparse.ArgumentParser(description='принимает строку и число')

    parser.add_argument('number', type=int, help='число')
    parser.add_argument('text', type=str, help='текст')
    parser.add_argument('--verbose', action='store_true', help='вывод доп. инфы')
    parser.add_argument('--repeat', type=int, default=1, help='количество повторений строки')

    args = parser.parse_args()

    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text = "{args.text}", repeat = {args.repeat}')

    print(f'Число: {args.number}, Строка: {args.text * args.repeat}')


if __name__ == "__main__":
    main()
