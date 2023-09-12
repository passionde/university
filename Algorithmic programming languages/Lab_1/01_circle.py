#!/usr/bin/env python3
# -*- coding: utf-8 -*-

radius = 42

# Площадь круга
print(round(radius * radius * 3.1415926, 4))


# Принадлежность точек кругу
point_1 = (23, 34)
print((point_1[0] ** 2 + point_1[1] ** 2) ** (1/2) <= radius)

point_2 = (30, 30)
print((point_2[0] ** 2 + point_2[1] ** 2) ** (1/2) <= radius)

