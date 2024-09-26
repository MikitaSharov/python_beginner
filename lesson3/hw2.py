# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
#
# Пример
#
# На входе:#
#
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:#
#
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

from string import punctuation

# text = 'Hello world. Hello Python. Hello again.'
text = text.lower().replace("'", " ")

for char in text:
    if char in punctuation:
        text = text.replace(char, '')

words = text.split()
temp_dict = {}
result_list = []

for word in words:
    if word.isalpha():
        if word in temp_dict:
            temp_dict[word] += 1
        else:
            temp_dict[word] = 1

temp_dict = sorted(temp_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)

result_list = list(temp_dict)

print(result_list[:10])
