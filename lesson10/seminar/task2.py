# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, *args):
        self.length = args[0]
        self.width = args[1] if len(args) > 1 else args[0]

    def perimeter(self):
        return 2 * (self.length + self.width)

    def square(self):
        return self.length * self.width
    
    @property
    def (self):
        return 
    
    @.setter
    def (self, value):
        pass
    
    @.deleter
    def (self):
        pass


rectangle = Rectangle(5, 4)
square = Rectangle(5)

print(rectangle.square())
print(rectangle.perimeter())
print(square.perimeter())
print(square.square())
