def calc_volume(a):
    """
    :param a: длина ребер
    :return: объем правильного тетраэдра
    """
    return 1 / 12 * (a ** 3) * (2 ** 0.5)


def calc_surface_area(a):
    """
    :param a: длина ребер
    :return: площадь поверхности правильного тетраэдра
    """
    return (3 ** 0.5) * (a ** 2)


def calc_weight(a, p):
    """
    :param a: длина ребер
    :param p: плотность вещества
    :return: массу правильного тетраэдра
    """
    return calc_volume(a) * p
