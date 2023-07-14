import math


def func_f(x):
    return math.pow(math.e, math.sin(x)) - x


def func_g(x):
    return math.log(1 + math.sqrt(x)) - math.cos(x)


def func_a_ij(i):
    return math.fabs(func_f(i) + func_g(i))


def func_n_a(m, n):
    m = min(m, n)
    max_value = float("-inf")

    for i in range(1, m+1):
        max_value = max(max_value, func_a_ij(i))

    return math.sqrt(max_value)


if __name__ == "__main__":
    print(func_n_a(1000, 1000))
