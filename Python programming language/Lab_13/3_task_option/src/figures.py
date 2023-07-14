import math
from abc import ABCMeta, abstractmethod


class BaseFigure(metaclass=ABCMeta):
    def calc_weight(self, p):
        return self.calc_volume() * p

    @abstractmethod
    def calc_volume(self):
        pass

    @abstractmethod
    def calc_surface_area(self):
        pass


class Parallelepiped(BaseFigure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def calc_volume(self):
        return self.a * self.b * self.h

    def calc_surface_area(self):
        return 2 * (self.a * self.b + self.b * self.h + self.h * self.a)


class Sphere(BaseFigure):
    def __init__(self, r):
        self.r = r

    def calc_volume(self):
        return (4 / 3) * math.pi * (self.r ** 3)

    def calc_surface_area(self):
        return 4 * math.pi * (self.r ** 2)


class Tetrahedron(BaseFigure):
    def __init__(self, a):
        self.a = a

    def calc_volume(self):
        return 1 / 12 * (self.a ** 3) * (2 ** 0.5)

    def calc_surface_area(self):
        return (3 ** 0.5) * (self.a ** 2)

