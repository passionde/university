#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_family = ["Мама", "Брат", "Сестра"]

my_family_height = [
    ["Мама", 150],
    ["Брат", 165],
    ["Сестра", 155]
]

print(f"Рост мамы - {my_family_height[0][1]} см")

print(f"Общий рост моей семьи - {sum([h[1] for h in my_family_height])} см")
