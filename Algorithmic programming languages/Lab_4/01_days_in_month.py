#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ls_30_days = [4, 6, 9, 11]

user_input = input("Введите, пожалуйста, номер месяца: ")

while user_input.isalpha():
    print(f'"{user_input}" не является числом')
    user_input = input("Введите, пожалуйста, номер месяца: ")

month = int(user_input)
print('Вы ввели', month)

if month == 2:
    print("В этом месяце 28 дней")
elif month > 12:
    print("Указан некорректный номер месяца")
elif month in ls_30_days:
    print("В этом месяце 30 дней")
else:
    print("В этом месяце 31 день")
