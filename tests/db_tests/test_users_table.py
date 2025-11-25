import psycopg2 as pq
import pytest
from faker import Faker

f = Faker()

# create connector, create cursor
dbname = 'postgres'
user = 'user'
password = 'pwd'
host = 'localhost'
port = 5433

@pytest.fixture
def cursor():
    # підєднатись до БД
    conn = pq.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    _cursor = conn.cursor()
    yield _cursor  # аналог return
    conn.commit()
    _cursor.close()
    conn.close()


def test_create_new_user(cursor):

    user_name = f.name()
    user_descr = f.job()

    insert_q = f"""INSERT INTO public.users
                    (name, description)
                    VALUES('{user_name}', '{user_descr}') returning id;"""

    cursor.execute(insert_q)

    user_id = cursor.fetchall()[0][0]  # returns [(some_id, )]

    cursor.execute(f'select name, description from public.users where id = {user_id}')

    created_name, created_description = cursor.fetchall()[0]  # [('Ashley Brown', 'Leisure centre manager')]

    # cursor.execute(f'select name, description from public.users')
    # cursor.fetchall()  # [('Ashley Brown', 'Leisure centre manager'), ('Jimmy Ryan', 'Immigration officer'), ...]

    assert user_name == created_name
    assert user_descr == created_description





