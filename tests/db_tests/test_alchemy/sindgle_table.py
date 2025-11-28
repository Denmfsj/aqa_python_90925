from sqlalchemy import create_engine, select, and_, or_, func, update, delete
from sqlalchemy.orm import sessionmaker

from core.db.tables.user_table import Base, OrmUser
from definitions import SQLITE_DB

from faker import Faker
import random

local_faker = Faker()

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
psql_str = "postgresql://user:pwd@localhost:5433/postgres"  # connection string
sqlite_str = f"sqlite:///{SQLITE_DB}"

engine = create_engine(psql_str)
engine_sqlite = create_engine(sqlite_str)

# Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine_sqlite)

Session = sessionmaker(bind=engine_sqlite)
session = Session()


# insert
new_users = []
for k in range(3):
    usr = OrmUser(name=local_faker.name(), age=random.choice(range(18, 100)))
    new_users.append(usr)


session.add_all(new_users)
session.commit()

#select всіх строк де id=6
# all_users = session.query(OrmUser).all()
# print(*all_users)

# top 10 yang  people
# select * from OrmUser order by age asc\desc
top_10_yang = session.query(OrmUser).order_by(OrmUser.age.desc()).limit(10).all()
print(*top_10_yang, sep='\n')

sum_id_ages_all_users = session.query(func.sum(OrmUser.age)).scalar()
print(sum_id_ages_all_users)

avg_age_all_users = session.query(func.avg(OrmUser.age)).scalar()
print(avg_age_all_users)


update_q =  update(OrmUser).where(OrmUser.age>60).values(age=60)
session.execute(update_q)

print(*session.query(OrmUser).filter_by(age=60).all(), sep='\n')


delete_q = delete(OrmUser).where(OrmUser.id>80)
session.execute(delete_q)
session.commit()


# user_with_id_6 = session.query(OrmUser).filter_by(id=6).first()
#
# print(user_with_id_6)
# print(user_with_id_6.id)
# print(user_with_id_6.name)
# print(user_with_id_6.age)
#
# user_with_id_6.age = 120
# session.commit()
# user_with_id_6 = session.query(OrmUser).filter_by(id=6).first()
# print(user_with_id_6)


# users_with_age_gte_60_q = select(OrmUser).where(OrmUser.age>60)  # підготовка запиту
# users_with_age_gte_60_r = session.execute(users_with_age_gte_60_q).all()  # виконати запит
#
# users_with_age_gte_60_and_end_n_q = select(OrmUser).where(OrmUser.age>60).where(OrmUser.name.endswith('n'))
# users_with_age_gte_60_and_end_n_r = session.execute(users_with_age_gte_60_and_end_n_q).all()  # виконати запит
#
# for u in users_with_age_gte_60_and_end_n_r:
#     print(u[0])

# users_with_age_gte_60_and_end_n_q = select(OrmUser).where(
#     # id > 20 AND (age > 80 OR name has nn)
#     and_(OrmUser.id>20,
#          or_(OrmUser.age>80, OrmUser.name.contains('nn'))
#     )
# )
# users_with_age_gte_60_and_end_n_r = session.execute(users_with_age_gte_60_and_end_n_q).all()  # виконати запит
# for u in users_with_age_gte_60_and_end_n_r:
#     print(u[0])

