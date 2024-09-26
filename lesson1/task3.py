# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

from math import factorial


class GeneratorFactorial:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration

        result = factorial(self.start)
        self.start += self.step

        return result


gen = GeneratorFactorial(5)
for res in gen:
    print(res)

print('\n')

gen2 = GeneratorFactorial(6, 2, 2)
for res in gen2:
    print(res)


