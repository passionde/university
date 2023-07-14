#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# I задание
print("______Бумага______")
tests = [
    (8, 9),
    (9, 8),
    (6, 8),
    (8, 6),
    (3, 4),
    (11, 9),
    (9, 11)
]

e_x, e_y = 10, 7

for p_x, p_y in tests:
    if min(e_x, e_y) > min(p_x, p_y) and max(e_x, e_y) > max(p_x, p_y):
        print("ДА")
    else:
        print("НЕТ")

# II задание
print("______Кирпич______")
tests = [
    (11, 10, 2),
    (11, 2, 10),
    (10, 11, 2),
    (10, 2, 11),
    (2, 10, 11),
    (2, 11, 10),
    (3, 5, 6),
    (3, 6, 5),
    (6, 3, 5),
    (6, 5, 3),
    (5, 6, 3),
    (5, 3, 6),
    (11, 3, 6),
    (3, 11, 6),
    (11, 6, 3),
    (6, 11, 3),
    (6, 3, 11),
    (3, 6, 11)
]

h_x, h_y = 8, 9

for brick_parameters in tests:
    brick_parameters = list(brick_parameters)
    brick_parameters.remove(max(*brick_parameters))

    if min(h_x, h_y) > min(*brick_parameters) and max(h_x, h_y) > max(*brick_parameters):
        print("ДА")
    else:
        print("НЕТ")
