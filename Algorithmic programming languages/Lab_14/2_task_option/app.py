import datetime

from sqlalchemy import create_engine

from src import database

engine = create_engine('sqlite:///sqlite3.db')
db = database.DataBase(engine)

print(
    """
____СПИСОК КОМАНД____
<Создание новых записей>
    1. Вид животного
    2. Добавить корм
    3. Добавить животное
    4. Назначить корм

<Выборка данных>
    5. Все животные
    6. Все корма

<Прочее>
    0. Выход
"""
)
while True:
    req = input("\nВыбор действия: ")

    if req == "1":
        title = input("  Название вида: ")
        db.add_kind_animal(title)

    elif req == "2":
        kind_feed = input("  Вид: ")
        manufacturer = input("  Производитель: ")
        title = input("  Наименование: ")

        price = input("  Цена: ")
        while price.isalpha():
            price = input("  Укажите цену числом: ")

        db.add_feed(kind_feed, manufacturer, title, price)

    elif req == "3":
        kinds = db.all_kinds()

        if not kinds:
            print("  Перед добавление животного, сначала добавьте хотя бы один вид")
            continue

        animal_name = input("  Кличка: ")

        date_of_birth = input("  Дата рождения (YYYY-MM-DD): ")
        while True:
            try:
                date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
                break
            except ValueError:
                date_of_birth = input("  Введите корректную дату в формате YYYY-MM-DD: ")

        gender = input("  Пол: ")

        print("  Выберите вид животного из списка:")
        for kind_id, title in kinds.items():
            print(f"    {kind_id} - {title}")

        kind_animal_id = input("  Номер вида: ")
        while kind_animal_id not in kinds:
            kind_animal_id = input("  Укажите номер из списка выше: ")

        db.add_animal(animal_name, date_of_birth, gender, kind_animal_id)

    elif req == "4":
        feeds = db.all_feeds()
        animals = db.all_animals()

        if not feeds and not animals:
            print("  Отсутствуют данные о корме и о животных. Сначала добавьте хотя бы по одной записи")
            continue
        elif not feeds:
            print("  Отсутствуют данные о корме. Сначала добавьте хотя бы одну запись")
            continue
        elif not animals:
            print("  Отсутствуют данные о животных. Сначала добавьте хотя бы одну запись")
            continue

        print("  Выберите животное из списка:")
        for animal_id, data in animals.items():
            print(f"    {animal_id} - {data['name']}")

        id_animal = input("  Номер животного: ")
        while id_animal not in animals:
            id_animal = input("  Укажите номер из списка выше: ")

        print("  Выберите корм из списка :")
        for feed_id, data in feeds.items():
            print(f"    {feed_id} - {data['title']}")

        id_feeds = input("  Номер корма (можно указать несколько): ").split()
        while True:
            is_valid = True

            for id_feed in id_feeds:
                if id_feed not in feeds:
                    print(f"    Номер {id_feed} отсутствует")
                    is_valid = False

            if is_valid:
                break

            id_feeds = input("  Укажите номера из списка выше : ").split()

        db.append_feeds_to_animal(id_animal, set(id_feeds))

    elif req == "5":
        animals = db.all_animals()

        if not animals:
            print("  Пока пусто")

        for id_animal, data in animals.items():
            print(f"  {id_animal}. {data['name']}")
            print(f"    Возраст: {data['age']}")
            print(f"    Пол: {data['gender']}")

            if not data["feeds"]:
                continue

            print("    Корм: ")
            for feed in data["feeds"]:
                print(f"      {feed['title']}, {feed['price']}₽")

    elif req == "6":
        feeds = db.all_feeds()

        if not feeds:
            print("  Пока пусто")

        for id_feed, data in feeds.items():
            title, price, count_animals = data.values()
            print(f"  {id_feed}. <{title}>, {price}₽, назначен {count_animals} животным")

    else:
        print("Введена неверная команда")
