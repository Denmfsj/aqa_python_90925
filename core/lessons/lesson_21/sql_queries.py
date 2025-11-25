create_tables = """CREATE TABLE public."users" (
	id int4 NOT NULL,
	description varchar NULL,
	CONSTRAINT user_pk PRIMARY KEY (id)
);
"""

insert_q = """
INSERT INTO public.users
(id, description)
VALUES(210, 'AQA');
"""

update_q = """update public.users
set description = 'New descr'
where id = 3"""

delete_q = """delete from public.users  where id = 3"""

foregin_key = """CREATE TABLE public.users_info (
	user_id int NOT NULL,
	user_phone varchar NOT NULL,
	CONSTRAINT users_info_pk PRIMARY KEY (user_id),
	CONSTRAINT users_info_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id)
);
"""


import psycopg2 as pq


# create connector, create cursor
dbname = 'postgres'
user = 'user'
password = 'pwd'
host = 'localhost'
port = 5433

conn = pq.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

# об'єкт який виконує запити і отримує результат
cursor = conn.cursor()

table_name = 'users'
create_tables = f"""CREATE TABLE public."{table_name}" (
	id int GENERATED ALWAYS AS IDENTITY NOT NULL,
	name varchar NULL,
	description varchar NULL,
	CONSTRAINT user_pk PRIMARY KEY (id)
);
"""


cursor.execute(f"drop table public.{table_name}")

cursor.execute(create_tables)
conn.commit()