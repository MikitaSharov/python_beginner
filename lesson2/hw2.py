from fractions import Fraction

frac1 = "1/7"
frac2 = "3/4"
divider1 = int(frac1.split('/')[1])
divider2 = int(frac2.split('/')[1])
numerator1 = int(frac1.split('/')[0])
numerator2 = int(frac2.split('/')[0])

print(f'Сумма дробей: {numerator1 * divider2 + numerator2 * divider1}/{divider1 * divider2}')
print(f'Произведение дробей: {numerator1 * numerator2}/{divider1 * divider2}')

print(f'Сумма дробей: {Fraction(frac1) + Fraction(frac2)}')
print(f'Произведение дробей: {Fraction(frac1) * Fraction(frac2)}')

s = "text text : one two three"
print(s.split(':')[0])
