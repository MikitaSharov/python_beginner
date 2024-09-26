# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
#
# На входе:
#
# lst = [1, 1, 2, 2, 3, 3]
# На выходе:
#
# [1, 2, 3]

lst = [1, 1, 2, 2, 3, 3]
copy_list = lst.copy()
result = []

for el in lst:
    if copy_list.count(el) == 2:
        result.append(el)
    copy_list.remove(el)

print(result)