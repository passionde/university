# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

sd.resolution = (1200, 600)

N = 20

len_snowflake = [randint(10, 100) for _ in range(N)]
cord_snowflake = [[randint(0, 1200), randint(500, 700)] for _ in range(N)]

while True:
    sd.clear_screen()

    for idx, cord in enumerate(cord_snowflake):
        point = sd.get_point(cord[0], cord[1])
        sd.snowflake(center=point, length=len_snowflake[idx])

        cord_snowflake[idx][1] -= randint(2, 20)
        cord_snowflake[idx][0] += randint(-10, 10)

        if cord_snowflake[idx][1] <= 0 or cord_snowflake[idx][0] > 1200:
            cord_snowflake[idx] = [randint(0, 1200), 600]

    sd.sleep(0.05)
    if sd.user_want_exit():
        break


sd.pause()

