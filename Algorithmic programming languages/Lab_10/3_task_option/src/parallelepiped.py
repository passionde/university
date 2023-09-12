def calc_volume(a, b, h):
    """
    :param a: длина параллелепипеда
    :param b: ширина параллелепипеда
    :param h: высота параллелепипеда
    :return: объем параллелепипеда
    """
    return a * b * h


def calc_surface_area(a, b, h):
    """
    :param a: длина параллелепипеда
    :param b: ширина параллелепипеда
    :param h: высота параллелепипеда
    :return: возвращает площадь поверхности параллелепипеда
    """
    return 2 * (a * b + b * h + h * a)


def calc_weight(a, b, h, p):
    """
    :param a: длина параллелепипеда
    :param b: ширина параллелепипеда
    :param h: высота параллелепипеда
    :param p: плотность вещества
    :return: возвращает массу параллелепипеда
    """
    return calc_volume(a, b, h) * p

