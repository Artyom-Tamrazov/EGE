for n in range(10000):
    # Перевод n в двоичную систему
    b = bin(n)[2:]
    sum_0 = 0
    sum_1 = 0
    for i in range(len(b)):
        if i % 2 != 0 and b[i] == '1':
            sum_1 += 1
        elif i % 2 == 0 and b[i] == '0':
            sum_0 += 1
    # abs() - модуль числа
    if abs(sum_1 - sum_0) == 5:
        print(n)
        break
