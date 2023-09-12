#!/usr/bin/env python3
# -*- coding: utf-8 -*-

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, "bear")
print(zoo)

birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

zoo.remove("elephant")
print(zoo)

print(f"Лев сидит в клетке номер {zoo.index('lion') + 1}")
print(f"Жаворонок сидит в клетке номер {zoo.index('lark') + 1}")
