def f(size):
    s = '1' * size
    while '111' in s or '222' in s:
        if '111' in s:
            s = s.replace('111', '22', 1)
        elif '222' in s:
            s = s.replace('222', '1', 1)
    return s

for n in range(200,1000):
    if f(n).count('1') == 0:
        print(n)
        break








