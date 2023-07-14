from collections import Counter


def city_letters_1(city: str):
    return ",".join([f"{let}:{'*'*count}" for let, count in Counter(city.lower().replace(" ", "")).items()])


def city_letters(city: str):
    city = city.replace(" ", "")
    city = city.lower()

    letters_count = {}
    for let in city:
        if let not in letters_count:
            letters_count[let] = 0

        letters_count[let] += 1

    result = []
    for let, count in letters_count.items():
        result.append(f"{let}:{'*'*count}")

    return ",".join(result)





print(city_letters("Chicago"))
print(city_letters("Bangkok"))
print(city_letters("Las Vegas"))