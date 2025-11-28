from sqlalchemy import Column, Integer, String

from .base_tables import Base

# Визначення моделі даних (таблиці) за допомогою класу
class OrmUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer, nullable=False)

    def __str__(self):
        return f'Raw row: id={self.id}, name={self.name}, age={self.age}'




