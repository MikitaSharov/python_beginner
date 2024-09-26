# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def len_circle(self):
        return 2 * pi * self.r

    def square_circle(self):
        return pi * self.r ** 2


circle = Circle(5)

print(f'{circle.len_circle():.2f}')
print(f'{circle.square_circle():.2f}')
