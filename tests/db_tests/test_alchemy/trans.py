from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from definitions import SQLITE_DB

# З'єднання з базою даних PostgreSQL (замініть дані на ваші)
DATABASE_URL = f"sqlite:///{SQLITE_DB}"
engine = create_engine(DATABASE_URL)

# Створення базового класу для визначення моделей даних
Base = declarative_base()

# Визначення моделі даних (таблиці) за допомогою класу
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

# Створення таблиці у базі даних
Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

new_product = Product(name='Laptop11', price=1000)
session.add(new_product)
session.commit()


try:
    # Початок транзакції
    session.begin()
    # Збільшення ціни для всіх продуктів на 10%
    session.query(Product).update({Product.price: Product.price * 1.1})

    # Збільшення ціни для конкретного продукту на 5%
    product = session.query(Product).filter_by(name='Laptop11').first()
    product.price *= 1.05
    raise AttributeError
    # Підтвердження транзакції
    session.commit()
except:
    # Скасування транзакції в разі виникнення помилки
    session.rollback()
    pass
finally:
    session.query(Product).update({Product.price: Product.price * 1.2})

    # Закриття сесії
    session.commit()