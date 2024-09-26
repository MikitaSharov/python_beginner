data = [1, 3.14, (1, 3.14), 'True', True]
for i, item in enumerate(data, start=1):

    print(f'{i}: {item} {id(item)} {item.__sizeof__()} {hash(item)} {"Целое число" if isinstance(item, int) \
        else "Строка" if isinstance(item, str) else ""}')





# help(enumerate)
