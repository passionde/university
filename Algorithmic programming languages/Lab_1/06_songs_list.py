#!/usr/bin/env python3
# -*- coding: utf-8 -*-

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

total_time = 0
for row in violator_songs_list:
    if row[0] in ['Halo', 'Enjoy the Silence', 'Clean']:
        total_time += row[1]
print(f"Три песни звучат {round(total_time, 2)} минут")


violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

total_time = 0
for song in ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']:
    total_time += violator_songs_dict.get(song, 0)

print(f"А другие три песни звучат {round(total_time)} минут")
