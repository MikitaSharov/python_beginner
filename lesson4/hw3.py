"""
У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, выполняя следующие операции, для выполнения которых необходимо написать следующие функции:
check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

Пополнение счета:
Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму. Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.

Снятие средств:
Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия также должна быть кратной MULTIPLICITY. При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:
Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:
Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.

Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.

Пример

На входе:

deposit(10000)
withdraw(4000)
exit()

print(operations)
На выходе:

['Пополнение карты на 10000 у.е. Итого 10000 у.е.',
 'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']

На входе:

deposit(1000)
withdraw(200)
exit()

print(operations)
На выходе:

['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.',
 'Возьмите карту на которой 770 у.е.']
На входе:

deposit(1000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)
На выходе:

['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.',
 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 440 у.е.', 'Пополнение карты на 500 у.е. Итого 940 у.е.',
 'Недостаточно средств. Сумма с комиссией 3045.000 у.е. На карте 940 у.е.', 'Возьмите карту на которой 940 у.е.']

На входе:

deposit(173)
withdraw(21)
exit()

print(operations)
На выходе:

Сумма должна быть кратной 50 у.е. Сумма должна быть кратной 50 у.е.
['Недостаточно средств. Сумма с комиссией 51 у.е. На карте 0 у.е.', 'Возьмите карту на которой 0 у.е.']
На входе:

deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)
На выходе:

['Пополнение карты на 1000000000000000 у.е. Итого 1000000000000000 у.е.',
 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 999999999999770 у.е.',
 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 999999999999440 у.е.',
 'Пополнение карты на 500 у.е. Итого 999999999999940 у.е.',
 'Снятие с карты 3000 у.е. Процент за снятие 45.000 у.е.. Итого 999999999996895.000 у.е.',
 'Вычтен налог на богатство 0.1% в сумме 99999999999689.5000 у.е. Итого 899999999997205.5000 у.е.',
 'Возьмите карту на которой 899999999997205.5000 у.е.']
 """

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
operations = []
count = 0


def check_multiplicity(amount):
    return amount % MULTIPLICITY == 0


def deposit(amount):
    global bank_account, operations

    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')


def withdraw(amount):
    global bank_account, operations
    tax_amount = amount * PERCENT_REMOVAL

    if tax_amount < MIN_REMOVAL:
        tax_amount = MIN_REMOVAL
    if tax_amount > MAX_REMOVAL:
        tax_amount = MAX_REMOVAL

    if check_multiplicity(amount):
        if amount + tax_amount <= bank_account:
            bank_account -= amount + tax_amount
            operations.append(
                f'Снятие с карты {amount} у.е. Процент за снятие {int(tax_amount)} у.е.. Итого {int(bank_account)} у.е.')
        else:
            operations.append(
                f'Недостаточно средств. Сумма с комиссией {int(amount + tax_amount)} у.е. На карте {bank_account} у.е.')
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        if amount + tax_amount >= bank_account:
            operations.append(f'Недостаточно средств. Сумма с комиссией {int(amount + tax_amount)} у.е. На карте {bank_account} у.е.')


def exit():
    global bank_account, operations

    if bank_account > RICHNESS_SUM:
        tax_amount = bank_account * RICHNESS_PERCENT
        bank_account -= tax_amount
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {tax_amount} у.е. Итого {bank_account} у.е.')

    operations.append(f'Возьмите карту на которой {bank_account} у.е.')


deposit(173)
withdraw(21)
exit()

print(operations)
