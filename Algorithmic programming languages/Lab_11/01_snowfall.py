# -*- coding: utf-8 -*-
import random

import simple_draw as sd


class Snowflake:
    def __init__(self, coordinates: list, length: int):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.coordinates = coordinates
        self.length = length

    def clear_previous_picture(self):
        # Очистка старой снежинки путем наложения новой снежинки цвета фона
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def move(self):
        # Изменение координат снежинки
        self.x += random.randint(0, 10)
        self.y -= random.randint(2, 20)

    def can_fall(self):
        return self.y > -self.length and self.x < sd.resolution[0] + self.length

    def draw(self):
        # Отрисовка снежинки на новом месте
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.COLOR_WHITE)


def get_flakes(count: int = 1):
    return_list = []

    for _ in range(count):
        # Генерация случайных координат на основе размера экрана
        coordinate = [random.randint(0, sd.resolution[0]), random.randint(sd.resolution[1] - 100, sd.resolution[1])]

        # Генерация случайного размера снежинки
        length = random.randint(10, 25)

        return_list.append(Snowflake(coordinate, length))

    return return_list


def append_flakes():
    new_flakes = []
    count = 0
    for f in flakes:
        if not f.can_fall():
            count += 1
        else:
            new_flakes.append(f)

    flakes.clear()
    flakes.extend(new_flakes)
    flakes.extend(get_flakes(count))


sd.resolution = (1200, 600)
flakes = get_flakes(count=20)  # создать список снежинок

while True:
    append_flakes()

    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()

    sd.sleep(0.01)
    if sd.user_want_exit():
        break

sd.pause()
