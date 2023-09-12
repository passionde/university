import math


def calc_volume(r):
    """
    :param r: радиус шара
    :return: объем шара
    """
    return (4 / 3) * math.pi * (r ** 3)


def calc_surface_area(r):
    """
    :param r: радиус шара
    :return: площадь поверхности шара
    """
    return 4 * math.pi * (r ** 2)


def calc_weight(r, p):
    """
    :param r: радиус шара
    :param p: плотность вещества
    :return: массу сферы
    """
    return calc_volume(r) * p
