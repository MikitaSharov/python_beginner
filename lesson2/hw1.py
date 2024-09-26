A = 10
B = 11
C = 12
D = 13
E = 14
F = 15

# num = 255
module_num = abs(num)
hexi = ''

if num == 0:
    print('0')

if isinstance(num, int):

    while module_num > 0:
        residue = module_num % 16

        if residue == A:
            hexi = 'A' + hexi
        elif residue == B:
            hexi = 'B' + hexi
        elif residue == C:
            hexi = 'C' + hexi
        elif residue == D:
            hexi = 'D' + hexi
        elif residue == E:
            hexi = 'E' + hexi
        elif residue == F:
            hexi = 'F' + hexi
        else:
            hexi = str(residue) + hexi

        module_num //= 16

    if num < 0:
        hexi = '-' + hexi

    print(f'Шестнадцатеричное представление числа: {hexi}')
    print(f'Проверка результата: {hex(num)}')
else:
    print("не целое число")
