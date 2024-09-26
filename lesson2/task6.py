# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import math

FREQUENCY = 50
PERCENT_TAX = 1.5
MIN_TAX = 30
MAX_TAX = 600
MIN_WITHDRAW = 2_000
MAX_WITHDRAW = 40_000
REWARD_PERCENT = 3
RICH_SUM = 5_000_000
RICH_TAX_PERCENT = 10
bank_account = 0
count = 0

print('+50: пополнить, -50: снять, 0: выход')
choose = input('1: Пополнить\n2: Снять\n0: Выход\n')

while True:
    print('+50: пополнить, -50: снять, 0: выход')
    choose = int(input())

    if choose == 0:
        break
    elif bank_account > RICH_SUM:
        bank_account -= bank_account * RICH_TAX_PERCENT / 100

    if not choose % FREQUENCY == 0:
        print(f'Сумма должна быть кратна {FREQUENCY}')
        continue

    if choose > 0:
        bank_account += choose
        count += 1

    if choose < 0 <= bank_account:
        choose *= -1

        if choose < MIN_WITHDRAW:
            if choose + MIN_TAX <= bank_account:
                bank_account = bank_account - choose - MIN_TAX
        elif choose > MAX_WITHDRAW:
            if choose + MAX_TAX <= bank_account
                bank_account = bank_account - choose - MAX_TAX
        else:
            if choose + choose * PERCENT_TAX / 100 <= bank_account:
                bank_account = bank_account - choose - choose * PERCENT_TAX / 100





print(bank_account)
quit()
