def sum_nested(l):
    s = 0
    for i in l:
        if isinstance(i, list):
            s += sum_nested(i)
        else:
            s += i
    return s


print(sum_nested([1, [2, [3, [4, 5]]]]))
