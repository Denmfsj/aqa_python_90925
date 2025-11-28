from sqlalchemy import create_engine, select, and_, or_, func, update, delete
from sqlalchemy.orm import sessionmaker

from core.db.tables.dep_table import Department
from core.db.tables.emp_table import Employee
from core.db.tables.base_tables import Base
from definitions import SQLITE_DB


from faker import Faker
import random

local_faker = Faker()

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
psql_str = "postgresql://user:pwd@localhost:5433/postgres"  # connection string
sqlite_str = f"sqlite:///{SQLITE_DB}"

engine_sqlite = create_engine(sqlite_str)

# Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine_sqlite)

Session = sessionmaker(bind=engine_sqlite)
session = Session()

# hr_dep = Department(name='HR')

dep = random.choice(session.query(Department).all())
emp = random.choice(session.query(Employee).all())

print(emp.id)
print(emp.name)
print(emp.department.id)
print(emp.department.name)

# user_anna = Employee(name=local_faker.name(), department=dep)
# session.add(user_anna)

# session.commit()