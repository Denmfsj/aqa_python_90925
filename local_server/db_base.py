import sqlite3
import time
import datetime
import pytz

from faker import Faker


dbname = 'new_db'
user = 'den'
password = 'den'
host = '127.0.0.1'
port = '5432'

class SQLiteConnector:

    def __init__(self, sqlite_path):
        self.sqlite_path = sqlite_path
        self.__connection = None
        self.__cursor = None


    def __enter__(self):
        self.__connection = sqlite3.connect(self.sqlite_path)
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = self.__connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__connection.close()

    def commit(self):
        self.__connection.commit()

    def execute(self, query):
        self.__cursor.execute(query)
        return [dict(row) for row in self.__cursor.fetchall()]


class SQLiteActions(SQLiteConnector):

    def __init__(self, sqlite_path, add_random_students=True):
        super().__init__(sqlite_path)
        with SQLiteConnector(self.sqlite_path) as c:
            c.execute(self.__create_student_tabel_query())
            if add_random_students:
                self.add_random_students(10)
            c.commit()


    @staticmethod
    def __create_student_tabel_query():
        return """CREATE TABLE IF NOT EXISTS student (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_date INTEGER NOT NULL,
    updated_date TEXT NOT NULL,
    score NUMERIC NOT NULL,
    score_name TEXT NOT NULL
);
"""

    def add_random_students(self, counts):
        with SQLiteConnector(self.sqlite_path) as c:
            for k in range(counts):
                name = Faker().name()
                score = Faker().random_int(1, 100)
                created_date = self.__get_created_date()
                updated_date = self.__get_updated_date()
                query = f"""
                INSERT INTO student (name, score, score_name, created_date, updated_date)
                VALUES ("{name}", {score}, "{self._get_score_name(score)}", 
                "{created_date}", "{updated_date}")
            """
                c.execute(query)
            c.commit()

    @staticmethod
    def __get_created_date():
        return time.time()  # UTC

    @staticmethod
    def __get_updated_date():
        local_tz = pytz.timezone('Europe/Kyiv')
        return datetime.datetime.now(local_tz).strftime("%Y-%m-%dT%H:%M:%S%z")

    def add_student(self, name, score, score_name=None):
        with SQLiteConnector(self.sqlite_path) as c:
            created_date = self.__get_created_date()
            updated_date = self.__get_updated_date()
            if not score_name:
                score_name = self._get_score_name(score)
            query = f"""
                            INSERT INTO student (name, score, score_name, created_date, updated_date)
                            VALUES ("{name}", {score}, "{score_name}", "{created_date}", "{updated_date}")
                        """
            c.execute(query)
            c.commit()

            # get last created row
            last_id = c.execute("SELECT last_insert_rowid()")[0]['last_insert_rowid()']
            return c.execute(f"SELECT * FROM student WHERE id = {last_id}")[0]

    def update_student(self, student_id, name=False, score=False, score_name=False):

        if not name and not score and not score_name:
            raise ValueError('You have to put name and/or score and/or score_name of the student')

        updates = []

        if name:
            updates.append(f'name = "{name}"')

        if score:
            updates.append(f'score = {score}')

        if score_name:
            updates.append(f'score_name = "{score_name}"')

        updates.append(f'updated_date = "{self.__get_updated_date()}"')

        query = f"""
            UPDATE student
            SET {', '.join(updates)}
            WHERE id = {student_id}
        """

        with SQLiteConnector(self.sqlite_path) as c:
            c.execute(query)
            c.commit()
            return self.get_student(student_id)

    def delete_student(self, student_id):

        query = f"""
            delete
            from student
            WHERE id = {student_id}
        """

        with SQLiteConnector(self.sqlite_path) as c:
            c.execute(query)
            c.commit()


    def get_students(self, limit: int = None, sort_by: str = None, sort_type: str = None):
        query = 'select * from student'

        if sort_by:
            query += f' order by "{sort_by}"'

            if sort_type:
                query += f' {sort_type}'

        if limit is not None:
            query += f' limit {limit};'

        print(query)

        with SQLiteConnector(self.sqlite_path) as c:
            return c.execute(query)


    def get_student(self, student_id):
        query = f'select * from student where id = {student_id}'

        with SQLiteConnector(self.sqlite_path) as c:
            return c.execute(query)[0]


    @staticmethod
    def _get_score_name(score):
        if score < 50:
            return 'BAD'
        elif score < 90:
            return 'GOOD'
        else:
            return 'GREAT'
