# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house: House | None = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды, поэтому...'.format(self.name), color='red')
            self.shopping()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились! Поэтому...'.format(self.name), color='red')
            self.work()

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def pick_up_cat(self, cat):
        """Подобрать кота"""
        cat.house = self.house
        cprint('У кота "{}" появился дом'.format(cat.name), color='cyan')

    def buy_cat_food(self):
        """Купить кошачий корм"""
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кормом для кота'.format(self.name), color='magenta')
            self.house.bowl += 50
            self.house.money -= 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        """Убраться в доме"""
        cprint('{} убрался в доме'.format(self.name), color='green')
        self.house.dirt -= 100
        self.fullness -= 20

        if self.house.dirt < 0:
            self.house.dirt = 0

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.bowl < 10:
            self.buy_cat_food()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class Cat:
    def __init__(self, name="Кот"):
        self.name = name
        self.fullness = 50
        self.house: House | None = None

    def __str__(self):
        return 'Я кот - {}, сытость {}'.format(self.name, self.fullness)

    def sleep(self):
        """Кот спит"""
        cprint('{} решил сегодня поспать'.format(self.name), color='green')
        self.fullness -= 10

    def eat(self):
        """Кот ест"""
        if self.house.bowl >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.bowl -= 10
        else:
            cprint('{} нет корма для кошек, поэтому...'.format(self.name), color='red')
            self.sleep()

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5

        cprint('{} расцарапал обои в доме'.format(self.name), color='yellow')

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 5)
        if self.fullness <= 20:
            self.eat()
        elif dice in [1, 2]:
            self.tear_wallpaper()
        elif dice == 3:
            self.eat()
        elif dice in [4, 5]:
            self.sleep()


class House:

    def __init__(self):
        # Для человека
        self.food = 50
        self.money = 0

        # Для кота
        self.bowl = 0
        self.dirt = 0

    def __str__(self):
        return f'В доме еды {self.food}, корма {self.bowl}, денег осталось {self.money}, мусора {self.dirt}'


print("\n\n\n\n\n\n\nНовая жизнь")
my_home = House()
citizen = Man("Марк")
cats = [Cat("Дарданелл"), Cat("Босфор"), Cat("Васька")]

citizen.go_to_the_house(my_home)
for cat in cats:
    citizen.pick_up_cat(cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    citizen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for cat in cats:
        print(cat)

    print(citizen)
    print(my_home)
