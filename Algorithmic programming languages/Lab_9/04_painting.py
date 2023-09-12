#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Lab_9.draw.nature
import Lab_9.draw.construction
import Lab_9.draw.other

import simple_draw as sd

from random import randint

sd.resolution = (1400, 800)


# Lab_9.draw.nature.rainbow((600, 500), length=500, angle=120)
# Lab_9.draw.construction.wall_brick((20, 20), (200, 100), (20, 10), width=1)
# Lab_9.draw.nature.tree(start_point=(300, 30), angle=90, length=100)
# Lab_9.draw.other.smile(40, 50)
# Lab_9.draw.nature.sun((200, 200), 50)


def build_home(start_point, size_wall, size_brick):
    # Стена
    Lab_9.draw.construction.wall_brick(start_point, size_wall, size_brick, width=1)

    # Крыша
    sd.polygon(
        [
            sd.get_point(
                start_point[0] - size_wall[0] // 10,
                start_point[1] + size_wall[1] - int(size_brick[1] * 0.5)
            ),

            sd.get_point(
                start_point[0] + (size_wall[0] // 10) + size_wall[0],
                start_point[1] + size_wall[1] - int(size_brick[1] * 0.5)
            ),

            sd.get_point(
                start_point[0] + size_wall[0] // 2,
                start_point[1] + int(size_wall[1] * 1.5)
            )
        ],
        sd.COLOR_DARK_RED,
        0
    )

    # Окно
    sd.rectangle(
        sd.get_point(start_point[0] + size_wall[0] // 4, start_point[1] + size_wall[1] // 3),
        sd.get_point(start_point[0] + size_wall[0] - size_wall[0] // 4, start_point[1] + size_wall[1] - size_wall[1] // 3),
        sd.COLOR_WHITE,
        0
    )


def people(x, y, color=sd.COLOR_CYAN):
    center = sd.get_point(x, y)
    center_body = sd.get_point(x, y - 70)
    end_body = sd.get_point(x, y - 120)

    sd.line(center, sd.get_point(x, y - 120), sd.COLOR_CYAN, width=3)

    sd.line(end_body, sd.get_point(x + 30, end_body.y - 75), sd.COLOR_CYAN, width=3)
    sd.line(end_body, sd.get_point(x - 30, end_body.y - 75), sd.COLOR_CYAN, width=3)

    sd.line(center_body, sd.get_point(x + 30, center_body.y - 50), sd.COLOR_CYAN, width=3)
    sd.line(center_body, sd.get_point(x - 30, center_body.y - 50), sd.COLOR_CYAN, width=3)

    sd.circle(center, radius=50, color=sd.background_color, width=0)
    Lab_9.draw.other.smile(x, y, color)


def snowdrift(x, y, count, radius):
    len_snowflake = [randint(5, 20) for _ in range(count)]
    cord_snowflake = [[randint(-radius + x, radius + x), randint(-radius + y, radius + y)] for _ in range(count)]

    for idx, cord in enumerate(cord_snowflake):
        point = sd.get_point(cord[0], cord[1])
        sd.snowflake(center=point, length=len_snowflake[idx], color=sd.COLOR_WHITE)


# Отрисовка земли
sd.rectangle(
    sd.get_point(0, 0),
    sd.get_point(sd.resolution[0], 80),
    sd.COLOR_DARK_ORANGE,
    0
)

# Отрисовка дома
build_home((300, 80), (400, 300), (20, 10))

# Отрисовка солнца
Lab_9.draw.nature.sun((200, 650), 70)

# Отрисовка дерева
Lab_9.draw.nature.tree(start_point=(1200, 80), angle=90, length=60)
Lab_9.draw.nature.tree(start_point=(1200, 80), angle=90, length=40)
Lab_9.draw.nature.tree(start_point=(1300, 90), angle=90, length=50)

# Отрисовка радуги
Lab_9.draw.nature.rainbow((sd.resolution[0], 500), length=600, angle=140, width=8)

# Человечек
people(900, 210)

# Сугроб
snowdrift(170, 150, 70, 70)

sd.pause()