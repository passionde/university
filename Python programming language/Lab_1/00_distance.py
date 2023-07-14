#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}

for city_1, cord_1 in sites.items():
    distances[city_1] = {}
    for city_2, cord_2 in sites.items():
        if city_1 == city_2:
            continue
        distances[city_1][city_2] = round(((cord_1[0] - cord_2[0]) ** 2 + (cord_1[1] - cord_2[1]) ** 2) ** 0.5, 3)

print(distances)




