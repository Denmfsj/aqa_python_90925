from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from .base_tables import Base

# Створення базового класу для визначення моделей даних


# Визначення моделей даних (таблиць) за допомогою класів
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee", back_populates="department")


# stud, cour

 # stud  <-> cours  !! wrong
 # stud <- relation  1-to-many
 # cours <- relation 1-to-many