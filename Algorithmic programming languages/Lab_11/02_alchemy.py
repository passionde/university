# -*- coding: utf-8 -*-

class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Вода"


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Воздух"


class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Огонь"


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Земля"


class Storm:
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Шторм"


class Steam:
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Пар"


class Dirt:
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Грязь"


class Lightning:
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Молния"


class Dust:
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Пыль"


class Lava:
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self

        return Unknown()

    def __str__(self):
        return "Лава"


class Unknown:
    def __add__(self, other):
        return self

    def __str__(self):
        return "&$#<D@)@_#JD_@"


#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава


print(Water(), '+', Air(), '=', Water() + Air())
print(Air(), '+', Water(), '=', Air() + Water())

print(Water(), '+', Water(), '=', Water() + Water())

print(Lava(), '+', Dust(), '=', Lava() + Dust())
