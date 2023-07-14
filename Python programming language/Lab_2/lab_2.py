# Найти все автоморфные числа в интервале от 1 до 1000.
# I вариант
result = []

for num in range(1, 1001):
    sqr_num = num * num
    if str(sqr_num).endswith(str(num)):
        result.append(str(num))

print(", ".join(result))


# II вариант
result = []
num = 1

while num <= 1000:
    sqr_num = num * num
    if str(sqr_num).endswith(str(num)):
        result.append(str(num))

    num += 1
print(", ".join(result))


# III вариант
result = []

mod = 10
for i in range(1, 1000):
    if i == mod:
        mod *= 10
    if (i * i) % mod == i:
        result.append(str(i))

print(", ".join(result))
