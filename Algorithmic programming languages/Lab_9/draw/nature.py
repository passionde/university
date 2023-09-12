import random

import simple_draw as sd


def rainbow(start_point, length=100, angle=60, width=4):
    rainbow_colors = (
        sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE
    )
    step = width + 1
    for color in rainbow_colors:
        v = sd.get_vector(sd.get_point(start_point[0], start_point[1] - step), length=length, angle=angle)
        v.draw(color=color, width=width)
        step += width + 1


def tree(start_point, angle, length):
    if length < 5:
        return

    start_point = sd.get_point(start_point[0], start_point[1])

    v1 = sd.get_vector(start_point=start_point, angle=angle + 30, length=length)
    v1.draw(width=1, color=sd.COLOR_GREEN if length <= 10 else sd.COLOR_DARK_ORANGE)

    v2 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length)
    v2.draw(width=1, color=sd.COLOR_GREEN if length <= 10 else sd.COLOR_DARK_ORANGE)

    r_angle_1 = random.randint(20, 25)
    r_angle_2 = random.randint(20, 25)

    r_length_1 = (random.randint(0, 15) * (-1 if random.randint(0, 1) else 1)) / 100
    r_length_2 = (random.randint(0, 15) * (-1 if random.randint(0, 1) else 1)) / 100

    tree((v1.end_point.x, v1.end_point.y), angle + r_angle_1, length * (0.75 + r_length_1))
    tree((v2.end_point.x, v2.end_point.y), angle - r_angle_2, length * (0.75 + r_length_2))

    # tree((v1.end_point.x, v1.end_point.y), angle + 30, length * 0.75)
    # tree((v2.end_point.x, v2.end_point.y), angle - 30, length * 0.75)


def sun(point, radius):
    center = sd.get_point(point[0], point[1])
    sd.circle(center, radius, width=0)

    for i in range(360 // 10, 361, 360 // 10):
        sd.get_vector(center, i, radius * 2).draw(width=3)
