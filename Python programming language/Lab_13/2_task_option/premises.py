from abc import ABCMeta, abstractmethod


class Premises(metaclass=ABCMeta):
    joule_per_meter = 100

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_heat_power(self):
        pass


class Room(Premises):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def calc_area(self):
        return round(self.width * self.length, 1)

    def calc_heat_power(self):
        return round(self.calc_area() * self.joule_per_meter)


class Apartment(Premises):
    def __init__(self, width, length, number_rooms):
        self.width = width
        self.length = length
        self.number_rooms = number_rooms

    def calc_area(self):
        return round(self.width * self.length * self.number_rooms, 1)

    def calc_heat_power(self):
        return round(self.calc_area() * self.joule_per_meter)


class House(Premises):
    def __init__(self, width, length, number_floors):
        self.width = width
        self.length = length
        self.number_floors = number_floors

    def calc_area(self):
        return round(self.width * self.length * self.number_floors, 1)

    def calc_heat_power(self):
        return round(self.calc_area() * self.joule_per_meter)