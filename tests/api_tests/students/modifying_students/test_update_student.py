from core.api.students_service.students_controller import StudentsController

from faker import Faker
import random
from assertpy import soft_assertions, assert_that

from core.api.students_service.stud_asserts import StAssert


class TestUpdateStudents:

    # students_ctrl = StudentsController()
    faker = Faker()

    def test_update_student_name(self, stud_ctrl, new_test_user_id):

        student_name = 'New test user name'

        # updating student
        updated_student = stud_ctrl.update_student(
            st_id=new_test_user_id,
            input_params={'name': student_name}
        )

        assert updated_student.get('id') == new_test_user_id, f'Expected id = {new_test_user_id}'
        assert updated_student.get('name') == student_name, f'New name must be {student_name}'


    def test_update_student_score(self, stud_ctrl, new_test_user_id):

        student_score = 99

        # updating student
        updated_student = stud_ctrl.update_student(
            st_id=new_test_user_id,
            input_params={'score': student_score}
        )

        assert updated_student.get('id') == new_test_user_id, f'Expected id = {new_test_user_id}'
        assert updated_student.get('score') == student_score, f'New Score must be {student_score}'




