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


shapes = {
    "0": triangle,
    "1": square,
    "2": pentagon,
    "3": hexagon
}

shapes_name = ("треугольник", "квадрат", "пятиугольник", "шестиугольник")

# Выывод возможных фигур
print("Возможные фигуры: ")
for i in range(len(shapes_name)):
    print(f"\t{i} : {shapes_name[i]}")

# Выбор фигуры
color_num = input("Введите номер желаемой фигуры > ")
while color_num not in shapes:
    print("Вы ввели некорректный номер!")
    color_num = input("Введите номер желаемой фигуры > ")

# Отрисовка выбранной фигуры
shapes[color_num](sd.get_point(300, 200), 100, 0)

sd.pause()
