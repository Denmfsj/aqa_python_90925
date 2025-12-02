from core.api.students_service.students_controller import StudentsController

from faker import Faker
import random
from assertpy import soft_assertions, assert_that

from core.api.students_service.stud_asserts import StAssert


class TestCreateStudents:

    students_ctrl = StudentsController()
    faker = Faker()

    def test_create_student(self):

        student_name = self.faker.name()
        student_score = random.choice(range(50,100))

        response = self.students_ctrl.create_student(
            {
                'name': student_name,
                'score': student_score
            }
        )

        assert response.status_code == 201, 'Status code must be 200'

        response_json = response.json()
        StAssert.base_check_student(response_json)

        with soft_assertions():

            assert_that(student_name,
                        f'Name must be {student_name}').is_equal_to(response_json.get('name'))
            assert_that(student_score,
                        f'score must be {student_score}').is_equal_to(response_json.get('score'))

