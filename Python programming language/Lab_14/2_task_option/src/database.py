from datetime import date

import sqlalchemy.engine
from sqlalchemy.orm import Session

from . import models


class DataBase:
    def __init__(self, engine: sqlalchemy.engine.Engine):
        self.engine = engine
        self.session = Session(bind=engine)

    def add_kind_animal(self, kind: str):
        new_kind = models.KindAnimal(title=kind)
        self.session.add(new_kind)
        self.session.commit()

    def add_feed(self, kind_feed, manufacturer, title, price):
        new_feed = models.Feed(
            kind_feed=kind_feed,
            manufacturer=manufacturer,
            title=title,
            price=price
        )

        self.session.add(new_feed)
        self.session.commit()

    def add_animal(self, name, date_of_birth, gender, id_kind):
        kinds = self.session.query(models.KindAnimal).filter(models.KindAnimal.id == id_kind)
        assert kinds.count(), f"id_kind <{id_kind}> not found"
        kind = kinds.first()

        new_animal = models.Animal(
            animal_name=name,
            date_of_birth=date_of_birth,
            gender=gender,
            kind_animal_id=kind
        )

        kind.animals.append(new_animal)

        self.session.add(new_animal)
        self.session.commit()

    def append_feeds_to_animal(self, id_animal, id_feeds):
        if not id_feeds:
            return

        feeds = self.session.query(models.Feed).filter(models.Feed.id.in_(id_feeds))
        assert feeds.count(), f"id_feeds {id_feeds} not found"

        animals = self.session.query(models.Animal).filter(models.Animal.id == id_animal)
        assert animals.count(), f"id_animal <{id_animal}> not found"
        animal = animals.first()

        for feed in feeds.all():
            animal.feeds.append(feed)

            self.session.add(feed)

        self.session.add(animal)
        self.session.commit()

    def all_animals(self):
        result = {}

        animals = self.session.query(models.Animal).all()
        for animal in animals:
            result[str(animal.id)] = {
                "name": animal.animal_name,
                "age": int((date.today() - animal.date_of_birth).days / 365.2425),
                "gender": animal.gender,
                "feeds": [
                    {
                        "title": feed.title,
                        "price": feed.price
                    } for feed in animal.feeds
                ]
            }

        return result

    def all_feeds(self):
        result = {}
        feeds = self.session.query(models.Feed).all()

        for feed in feeds:
            result[str(feed.id)] = {
                "title": feed.title,
                "price": feed.price,
                "count_animals": len(feed.animals)  # feed.animals == [models.Animal]
            }

        return result

    def all_kinds(self):
        kinds = self.session.query(models.KindAnimal).all()

        return {str(i.id): i.title for i in kinds}


