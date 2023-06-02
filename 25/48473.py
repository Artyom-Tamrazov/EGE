from fnmatch import fnmatch

for n in range(0, 10 ** 10, 3023):
    # Функция, проверяющая, соответствует ли строка шаблону
    if fnmatch(str(n), '1?954*21'):
        print(n)
