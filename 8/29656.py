import itertools

var = itertools.product("АНДРЕЙ", repeat=7)
count = 0
for i in var:
    line = ''.join(i)
    if line.count('А') == 1 and line.count('Й') == 1 and line[0] != "Й":
        count += 1
print(count)
