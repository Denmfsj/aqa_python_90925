import pytest
import sqlite3
from core.api.students_service.students_controller import StudentsController
from definitions import SQLITE_STUDENT_APP_DB
from faker import Faker


# function -default, 1 тест(функція)
# class, 1 класс з тестамии
# module, 1 файл
# package, 1 папка
# session, всі тести


@pytest.fixture
def random_student_name():
    faker = Faker()
    student_name = f'aqa_test_{str(faker.name())}'
    return student_name

@pytest.fixture(scope='session')
def stud_ctrl():
    print('Executing stud_ctrl fixture')
    st_ctrl = StudentsController()
    return st_ctrl

@pytest.fixture(scope='session', autouse=True)
def cleaning_db():
    yield
    print('\n\n!--------------------------Cleaning db--------------------------!\n\n')

    conn = sqlite3.connect(SQLITE_STUDENT_APP_DB)
    cursor = conn.cursor()

    # видалити всіх стедетнів ім'я яких з aqa_test_
    cursor.execute(f'delete from student where name like "aqa_test_%"')

    conn.commit()
    cursor.close()
    conn.close()


# @pytest.fixture
# def cleaning_db_after_test_dev():
#     yield
#     print('\n\n!--------------------------Cleaning db cleaning_db_after_test_dev--------------------------!\n\n')
#
#     conn = sqlite3.connect(SQLITE_STUDENT_APP_DB)
#     cursor = conn.cursor()
#
#     # видалити всіх стедетнів ім'я яких з aqa_test_
#     cursor.execute(f'delete from student where name like "aqa_test_%"')
#
#     conn.commit()
#     cursor.close()
#     conn.close()
#
#
# @pytest.fixture
# def cleaning_db_after_test_stage():
#     yield
#     print('\n\n!--------------------------Cleaning db cleaning_db_after_test_stage--------------------------!\n\n')
#
#     conn = sqlite3.connect(SQLITE_STUDENT_APP_DB)
#     cursor = conn.cursor()
#
#     # видалити всіх стедетнів ім'я яких з aqa_test_
#     cursor.execute(f'delete from student where name like "aqa_test_%"')
#
#     conn.commit()
#     cursor.close()
#     conn.close()

