from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

# color -> position
# product -> teacher
# category -> department


teacher_department = Table(
    'teacher_department', Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teachers.id")),
    Column("department_id", Integer, ForeignKey("departments.id"))
)


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    position_name = Column(String)

    teachers = relationship("Teacher")


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String)

    birth_date = Column(Date)

    position_id = Column(Integer, ForeignKey('positions.id'))
    departments = relationship("Department", secondary=teacher_department, backref=backref("teachers"))


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    department_name = Column(String)
    institute_name = Column(String)


