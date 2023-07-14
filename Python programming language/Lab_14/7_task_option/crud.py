from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from Lab_14.var_7 import models


engine = create_engine('sqlite:///sqlite3.db')
session = Session(bind=engine)


def add_kind_control(kind):
    new_kind = models.KindControl(title=kind)
    session.add(new_kind)
    session.commit()


def add_teacher(full_name):
    new_teacher = models.Teacher(full_name=full_name)
    session.add(new_teacher)
    session.commit()


def add_discipline(id_kind, discipline_name, lectures, practices, laboratory):
    kinds = session.query(models.KindControl).filter(models.KindControl.id == id_kind)
    assert kinds.count(), f"id_kind <{id_kind}> not found"
    kind = kinds.first()

    new_discipline = models.Discipline(
        discipline_name=discipline_name,
        lectures=lectures,
        practices=practices,
        laboratory=laboratory,
        kind_control_id=kind
    )

    kind.disciplines.append(new_discipline)

    session.add(new_discipline)
    session.commit()


def append_teachers_to_disciplines(id_discipline, id_teachers):
    teachers = session.query(models.Teacher).filter(models.Teacher.id.in_(id_teachers))
    assert teachers.count(), f"id_feeds {id_teachers} not found"

    disciplines = session.query(models.Discipline).filter(models.Discipline.id == id_discipline)
    assert disciplines.count(), f"id_animal <{id_discipline}> not found"
    discipline = disciplines.first()

    for teacher in teachers.all():
        discipline.teachers.append(teacher)

        session.add(teacher)

    session.add(discipline)
    session.commit()


def all_disciplines():
    disciplines = session.query(models.Discipline).all()
    print("Все дисциплины:")
    for discipline in disciplines:
        print(f"\t<{discipline.discipline_name}>")

        print("\tПреподаватели:")
        for teacher in discipline.teachers:
            print(f"\t\t{teacher.full_name}")

        kind = session.query(models.KindControl).filter(models.KindControl.id == discipline.kind_control_id)
        print(f"\tВид контроля: {kind.first().title}\n")


def all_teachers():
    teachers = session.query(models.Teacher).all()

    print("Все преподаватели:")
    for teacher in teachers:
        print(f"\tФИО: {teacher.full_name}, число дисциплин: {len(teacher.disciplines)}")
