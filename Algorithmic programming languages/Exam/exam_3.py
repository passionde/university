def rec(n):
    if n < 10:
        return n

    temp = n
    digits = 0
    while temp > 9:
        temp = temp // 10
        digits += 1

    return (n % 10) * (10 ** digits) + rec(n // 10)


print(rec(1234))