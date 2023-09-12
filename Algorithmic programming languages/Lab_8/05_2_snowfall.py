# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

sd.resolution = (1200, 600)

N = 20

len_snowflake = [randint(10, 100) for _ in range(N)]
cord_snowflake = [[randint(0, 1200), randint(500, 700)] for _ in range(N)]

while True:
    sd.start_drawing()

    for idx, cord in enumerate(cord_snowflake):
        point = sd.get_point(cord[0], cord[1])
        sd.snowflake(center=point, length=len_snowflake[idx], color=sd.background_color)

        cord_snowflake[idx][1] -= randint(2, 20)
        cord_snowflake[idx][0] += randint(-10, 10)

        if cord_snowflake[idx][1] <= 5 or cord_snowflake[idx][0] > 1500:
            cord_snowflake[idx] = [randint(0, 1200), 600]

        point = sd.get_point(cord[0], cord[1])
        sd.snowflake(center=point, length=len_snowflake[idx], color=sd.COLOR_WHITE)

    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break


sd.pause()

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

