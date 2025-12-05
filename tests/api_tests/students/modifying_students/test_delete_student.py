from core.api.students_service.students_controller import StudentsController

from faker import Faker
import pytest
from assertpy import soft_assertions, assert_that

from core.api.students_service.stud_asserts import StAssert
from utils.settings import d_settings


class TestDeleteStudents:

    # students_ctrl = StudentsController()
    faker = Faker()

    def test_delete_student(self, stud_ctrl, new_test_user_id):

        # видалення студента
        stud_ctrl.delete_student(st_id=new_test_user_id)

    #
    #
    # # @pytest.mark.usefixtures(f"cleaning_db_after_test_{d_settings.current_env}")  #
    # def test_delete_student_params(self, stud_ctrl, new_test_user_id):
    #
    #     # видалення студента
    #     stud_ctrl.delete_student(st_id=new_test_user_id)





