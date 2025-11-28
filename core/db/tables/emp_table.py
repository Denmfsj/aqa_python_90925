from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from .base_tables import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("Department", back_populates="employees")