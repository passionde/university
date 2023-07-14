import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import models


engine = create_engine('sqlite:///sqlite3.db')
session = Session(bind=engine)


def create_all():
    models.Base.metadata.create_all(bind=engine)


def add_position(position_name):
    new_position = models.Position(position_name=position_name)
    session.add(new_position)
    session.commit()


def add_department(department_name, institute_name):
    new_department = models.Department(department_name=department_name, institute_name=institute_name)
    session.add(new_department)
    session.commit()


def add_teacher(name, birth_date, position_id, departments_id):
    # Создание записи о новом преподавателе
    positions = session.query(models.Position).filter(models.Position.id == position_id)
    assert positions.count(), f"Должности с ID:<{position_id}> не найдено"
    position = positions.first()

    new_teacher = models.Teacher(
        teacher_name=name,
        birth_date=datetime.datetime.strptime(birth_date, "%Y-%m-%d").date(),
        position_id=position
    )

    position.teachers.append(new_teacher)

    # Установка кафедры
    departments = session.query(models.Department).filter(models.Department.id.in_(departments_id))
    assert departments.count(), f"В переданном списке ID :{departments} не найдено ни одного значения в БД"

    for department in departments.all():
        new_teacher.departments.append(department)
        session.add(department)

    session.add(new_teacher)
    session.commit()


def all_teachers():
    teachers = session.query(models.Teacher).all()
    today = datetime.date.today()
    print("Все преподаватели:")
    for teacher in teachers:
        position = session.query(models.Position).filter(models.Position.id == teacher.position_id).first()
        age = today.year - teacher.birth_date.year - ((today.month, today.day) < (teacher.birth_date.month, teacher.birth_date.day))
        departments = [department.department_name for department in teacher.departments]

        print(f"{teacher.teacher_name.title()}, возраст: {age}, должность: {position.position_name},  кафедра(-ы): {', '.join(departments)}")


def all_departments():
    departments = session.query(models.Department).all()
    print("Все кафедры (название -> число преподавателей):")
    for department in departments:
        print(f"\t{department.department_name} ({department.institute_name}) -> {len(department.teachers)}")