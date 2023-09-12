#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Lab_9.my_burger.functions as burger_func


def double_cheeseburger():
    print("Приготовим двойной чизбургер...")
    burger_func.adding_bun()
    burger_func.adding_cutlets()
    burger_func.adding_cheese()
    burger_func.adding_cheese()
    burger_func.adding_cucumber()
    burger_func.adding_mayonnaise()
    burger_func.adding_bun()


def my_burger():
    print("Приготовим бургер по моему рецепту...")
    burger_func.adding_bun()
    print("Нужно больше мяса!")
    burger_func.adding_cutlets()
    burger_func.adding_cutlets()
    burger_func.adding_cheese()
    burger_func.adding_cucumber()
    burger_func.adding_mayonnaise()
    burger_func.adding_bun()

my_burger()
