# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, first_name, last_name, middle_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


person = Person("Иван", "Иванов", "Иванович", 30)

print(person._age)
person.birthday()
print(person._age)
person.age = 1
print(person.age)
