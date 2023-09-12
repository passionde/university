#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}


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

# Рассчитать на какую сумму лежит каждого товара на складе

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price'] * lamps_quantity
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


table_quantity = store[goods['Стол']][0]['quantity']
table_quantity1 = store[goods['Стол']][1]['quantity']
table_price = store[goods['Стол']][0]['price']
table_price1 = store[goods['Стол']][1]['price']

table_cost = table_quantity * table_price + table_quantity1 * table_price1
print('Стол -', table_quantity + table_quantity1, 'шт, стоимость', table_cost, 'руб')

sofa_quantity = store[goods['Диван']][0]['quantity']
sofa_quantity1 = store[goods['Диван']][1]['quantity']
sofa_price = store[goods['Диван']][0]['price']
sofa_price1 = store[goods['Диван']][1]['price']

sofa_cost = sofa_quantity * sofa_price + sofa_quantity1 * sofa_price1
print('Диван -', sofa_quantity + sofa_quantity1, 'шт, стоимость', sofa_cost, 'руб')

chair_quantity = store[goods['Стул']][0]['quantity']
chair_quantity1 = store[goods['Стул']][1]['quantity']
chair_quantity2 = store[goods['Стул']][2]['quantity']
chair_price = store[goods['Стул']][0]['price']
chair_price1 = store[goods['Стул']][1]['price']
chair_price2 = store[goods['Стул']][2]['price']
print(chair_quantity, chair_price, chair_quantity1, chair_price1, chair_quantity2, chair_price2)

chair_cost = chair_quantity * chair_price + chair_quantity1 * chair_price1 + chair_quantity2 * chair_price2
print('Стул -', chair_quantity + chair_quantity1 + chair_quantity2, 'шт, стоимость', chair_cost, 'руб')
