import pytest
import random
from requests.auth import HTTPBasicAuth

# response = requests.post('http://127.0.0.1:8080/auth', auth=HTTPBasicAuth('test_user', 'test_pass') )

# function -default, 1 тест(функція)
# class, 1 класс з тестамии
# module, 1 файл
# package, 1 папка
# session, всі тести


# stud_ctrl = session
# random_student_name = function

# new_test_user_id scope = function


@pytest.fixture  # scope=function
def new_test_user_id(stud_ctrl, random_student_name):

    student_score = random.choice(range(50,100))


    print('creating student')
    # create student
    response_json = stud_ctrl.create_student(
        {
            'name': random_student_name,
            'score': student_score
        }
    )

    # new data
    stud_id = response_json.get('id')
    print(f'Student was created, id: {stud_id}')
    yield stud_id

    # видалення студента
    print(f'Deleting student, id: {stud_id}')
    stud_ctrl.delete_student(st_id=stud_id)

