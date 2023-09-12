#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50

diff = -50
for y in range(0, 601, 50):
    diff += 50
    for x in range(0, 1201, 100):
        sd.rectangle(sd.get_point(x - 100 - diff, y - 50), sd.get_point(x - diff, y), color=sd.COLOR_ORANGE, width=2)

sd.pause()
