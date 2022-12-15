# Подбираем A
for a in range(32):
    # Флаг
    f = True
    # При всех x формула не должна ни разу вернуть false
    for x in range(32):
        # Обратная формула not( формула из задания )
        if not ((x & 29 != 0) <= ((x & 12 == 0) <= (x & a != 0))):
            f = False
    if f:
        print(a)
        break
