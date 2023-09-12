#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

names_products = {value: key for key, value in goods.items()}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key, item in store.items():
    # Определение наименования
    name_product = names_products.get(key)

    # Подсчет статистики
    total_quantity = 0
    total_cost = 0
    for order in item:
        total_quantity += order.get('quantity', 0)
        total_cost += order.get('price', 0) * order.get('quantity', 0)

    # Форматированный вывод
    print(f"{name_product} - {total_quantity} шт, стоимость {total_cost} руб")


