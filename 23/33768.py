"""
Исполнитель преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:

1. Прибавить 1
2. Прибавить 2
3. Умножить на 3

Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2, третья — умножает на 3.
Программа для исполнителя — это последовательность команд. Сколько существует программ,
которые преобразуют исходное число 2 в число 16, и при этом траектория вычислений содержит число 11 и не содержит числа 15?
"""


def f(x, y):
    # Ограничение "не содержит числа"
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


# Ограничение "содержит число"
print(f(2, 11) * f(11, 16))
