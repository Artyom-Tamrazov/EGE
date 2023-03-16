"""
    Вариант, когда парой являются два соседних числа
"""
# Открытие файла
f = open('38951.txt')
# Чтение файла в массив целиком
nums = list(map(int, f.readlines()))
count = 0
m = 0
for i in range(len(nums) - 1):
    if (nums[i] % 3 == 0 or nums[i + 1] % 3 == 0) and (nums[i] + nums[i + 1]) % 5 == 0:
        count += 1
        m = max(m, nums[i] + nums[i + 1])
print(count, m)
