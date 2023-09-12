def squares_needed(n):
    if n == 0:
        return n

    count = 1
    steps = 1
    while True:
        if count >= n:
            return steps

        count += 2 ** steps
        steps += 1


for n in [0, 1, 2, 3, 4, 9, 3000]:
    print(f"Для {n} - {squares_needed(n)} клетки(-ок)")
