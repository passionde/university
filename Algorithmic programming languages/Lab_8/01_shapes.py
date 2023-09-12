# -*- coding: utf-8 -*-
import time

import simple_draw as sd


# 1 часть
def triangle(point: sd.Point, length, angle=0):
    cur_point = point

    for i in range(0, 361, 120):
        v = sd.get_vector(start_point=cur_point, angle=angle + i, length=length, width=3)
        cur_point = v.end_point
        v.draw()


def square(point: sd.Point, length, angle=0):
    cur_point = point

    for i in range(0, 361, 90):
        v = sd.get_vector(start_point=cur_point, angle=angle + i, length=length, width=3)
        cur_point = v.end_point
        v.draw()


def pentagon(point: sd.Point, length, angle=0):
    cur_point = point

    for i in range(0, 361, 72):
        v = sd.get_vector(start_point=cur_point, angle=angle + i, length=length, width=3)
        cur_point = v.end_point
        v.draw()


def hexagon(point: sd.Point, length, angle=0):
    cur_point = point

    for i in range(0, 361, 60):
        v = sd.get_vector(start_point=cur_point, angle=angle + i, length=length, width=3)
        cur_point = v.end_point
        v.draw()

# triangle(sd.get_point(100, 50), 100, 30)
# square(sd.get_point(400, 50), 100, 30)
# pentagon(sd.get_point(100, 300), 100, 30)
# hexagon(sd.get_point(400, 300), 100, 30)



# 2 часть
def draw_n_gon(point: sd.Point, length: int, angle, count_angle):
    """
    Рисует равносторонний n-угольник

    :param point: Точка начала рисунка
    :param length: Длина сторон n-угольника
    :param angle: Угол отклонения
    :param count_angle: Количество углов
    """
    assert count_angle >= 3, "The number of corners must be equal to or greater than three"

    cur_point = point  # Текущее положение точки
    offset = 360 % count_angle != 0  # Флаг наличия смещения
    offset_angle = round(360 / count_angle)  # Угол разворота для отображения n-угольника
    v = None  # Чтобы IDE не злилось)

    # Если есть смещение, то рисуется на одну сторону меньше
    for i in range(0, count_angle - offset):
        v = sd.get_vector(start_point=cur_point, angle=angle + i * offset_angle, length=length, width=3)
        cur_point = v.end_point
        v.draw()

    # Соединение обрыва
    if offset:
        sd.line(point, v.end_point, width=3)


def triangle(point: sd.Point, length, angle=0):
    draw_n_gon(point, length, angle, 3)


def square(point: sd.Point, length, angle=0):
    draw_n_gon(point, length, angle, 4)


def pentagon(point: sd.Point, length, angle=0):
    draw_n_gon(point, length, angle, 5)


def hexagon(point: sd.Point, length, angle=0):
    draw_n_gon(point, length, angle, 6)


def test_draw_n_gon(point: sd.Point, length, angle=0):
    draw_n_gon(point, length, angle, 11)


triangle(sd.get_point(100, 50), 100, 30)
square(sd.get_point(400, 50), 100, 30)
pentagon(sd.get_point(100, 300), 100, 30)
hexagon(sd.get_point(400, 300), 100, 30)

# Тестирование соединения
test_draw_n_gon(sd.get_point(300, 200), 100, 30)


sd.pause()
