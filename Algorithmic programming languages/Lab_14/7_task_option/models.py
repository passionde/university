from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()
engine = create_engine('sqlite:///sqlite3.db')

primary_key_kwargs = {
    "nullable": False,
    "unique": True,
    "primary_key": True,
    "autoincrement": True
}

discipline_teacher = Table(
    'discipline_teacher', Base.metadata,
    Column("discipline_id", Integer(), ForeignKey("discipline.id")),
    Column("teacher_id", Integer(), ForeignKey("teacher.id"))
)


class Discipline(Base):
    __tablename__ = "discipline"

    id = Column(Integer, **primary_key_kwargs)

    discipline_name = Column(String())
    lectures = Column(Integer())
    practices = Column(Integer())
    laboratory = Column(Integer())

    kind_control_id = Column(Integer, ForeignKey("kind_control.id"))
    teachers = relationship("Teacher", secondary=discipline_teacher, backref=backref('disciplines'))


class KindControl(Base):
    __tablename__ = "kind_control"

    id = Column(Integer, **primary_key_kwargs)
    title = Column(String(), unique=True)

    disciplines = relationship("Discipline")


class Teacher(Base):  # Feed
    __tablename__ = "teacher"

    id = Column(Integer, **primary_key_kwargs)
    full_name = Column(String())



Base.metadata.create_all(bind=engine)
