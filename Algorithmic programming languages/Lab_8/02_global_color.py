# -*- coding: utf-8 -*-
import simple_draw as sd


def draw_n_gon(point: sd.Point, length: int, angle, count_angle, color):
    """
    Рисует равносторонний n-угольник

    :param point: Точка начала рисунка
    :param length: Длина сторон n-угольника
    :param angle: Угол отклонения
    :param count_angle: Количество углов
    :param color: Цвет фигур
    """
    assert count_angle >= 3, "The number of corners must be equal to or greater than three"

    cur_point = point  # Текущее положение точки
    offset = 360 % count_angle != 0  # Флаг наличия смещения
    offset_angle = round(360 / count_angle)  # Угол разворота для отображения n-угольника
    v = None  # Чтобы IDE не злилось)

    # Если есть смещение, то рисуется на одну сторону меньше
    for i in range(0, count_angle - offset):
        v = sd.get_vector(start_point=cur_point, angle=angle + i * offset_angle, length=length)
        cur_point = v.end_point
        v.draw(width=3, color=color)

    # Соединение обрыва
    if offset:
        sd.line(point, v.end_point, width=3)


def triangle(point: sd.Point, length, angle=0, color=sd.COLOR_YELLOW):
    draw_n_gon(point, length, angle, 3, color)


def square(point: sd.Point, length, angle=0, color=sd.COLOR_YELLOW):
    draw_n_gon(point, length, angle, 4, color=color)


def pentagon(point: sd.Point, length, angle=0, color=sd.COLOR_YELLOW):
    draw_n_gon(point, length, angle, 5, color=color)


def hexagon(point: sd.Point, length, angle=0, color=sd.COLOR_YELLOW):
    draw_n_gon(point, length, angle, 6, color=color)


colors = {
    "0": sd.COLOR_RED,
    "1": sd.COLOR_ORANGE,
    "2": sd.COLOR_YELLOW,
    "3": sd.COLOR_GREEN,
    "4": sd.COLOR_CYAN,
    "5": sd.COLOR_BLUE,
    "6": sd.COLOR_PURPLE
}

colors_name = ("red", "orange", "yellow", "green", "cyan", "blue", "purple")

# Выывод возможных цветов
print("Возможные цвета: ")
for i in range(len(colors_name)):
    print(f"\t{i} : {colors_name[i]}")

# Выбор цвета
color_num = input("Введите номер желаемого цвета > ")
while color_num not in colors:
    print("Вы ввели некорректный номер!")
    color_num = input("Введите номер желаемого цвета > ")

color_default = colors[color_num]

# Отрисовка фигур
triangle(sd.get_point(100, 50), 100, 30, color_default)
square(sd.get_point(400, 50), 100, 30, color_default)
pentagon(sd.get_point(100, 300), 100, 30, color_default)
hexagon(sd.get_point(400, 300), 100, 30, color_default)


sd.pause()
