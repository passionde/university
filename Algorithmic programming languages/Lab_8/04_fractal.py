# -*- coding: utf-8 -*-
import random

import simple_draw as sd


# def draw_branches(point, angle, length):
#     """1 задание"""
#     sd.get_vector(start_point=point, angle=angle + 30, length=length).draw(width=3)
#     sd.get_vector(start_point=point, angle=angle - 30, length=length).draw(width=3)

# def draw_branches(start_point, angle, length):
#     """2 задание"""
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=start_point, angle=angle + 30, length=length)
#     v1.draw(width=1)
#
#     v2 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length)
#     v2.draw(width=1)
#
#     draw_branches(v1.end_point, angle + 30, length * 0.75)
#     draw_branches(v2.end_point, angle - 30, length * 0.75)

def draw_branches(start_point, angle, length):
    """3 задание"""
    if length < 3:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle + 30, length=length)
    v1.draw(width=1)

    v2 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length)
    v2.draw(width=1)

    r_angle_1 = random.randint(24, 36)
    r_angle_2 = random.randint(24, 36)

    r_length_1 = (random.randint(0, 20) * (-1 if random.randint(0, 1) else 1)) / 100
    r_length_2 = (random.randint(0, 20) * (-1 if random.randint(0, 1) else 1)) / 100

    draw_branches(v1.end_point, angle + r_angle_1, length * (0.75 + r_length_1))
    draw_branches(v2.end_point, angle - r_angle_2, length * (0.75 + r_length_2))


root_point = sd.get_point(300, 30)
draw_branches(start_point=root_point, angle=90, length=100)


sd.pause()
