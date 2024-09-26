# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

from math import factorial


class Factorial:
    def __init__(self, k):
        self.k = k
        self.history = []

    def __call__(self, num):
        result = factorial(num)
        self.history.append({num: result})

        if len(self.history) > self.k:
            self.history.pop(0)

        return result

    @property
    def get_history(self):
        return self.history


fact = Factorial(3)
fact(5)
fact(4)
fact(3)
print(*fact.get_history)

fact(6)
print(*fact.get_history)
