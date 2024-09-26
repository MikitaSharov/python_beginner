from math import factorial
from json import dump


class Factorial:
    def __init__(self, k):
        self.k = k
        self.history = []
        self.FILE_PATH = './factorial.json'

    def __call__(self, num):
        result = factorial(num)
        self.history.append({num: result})

        if len(self.history) > self.k:
            self.history.pop(0)

        return result

    @property
    def get_history(self):
        return self.history

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.FILE_PATH, 'w') as file:
            dump(self.get_history, file, indent=4)


with Factorial(3) as fact:
    fact(5)
    fact(4)
    fact(3)
    fact(6)
