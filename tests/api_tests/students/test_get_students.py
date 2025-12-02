from core.api.students_service.students_controller import StudentsController
from assertpy import assert_that, soft_assertions
from core.api.students_service.stud_asserts import StAssert


class TestGetStudents:

    students_ctrl = StudentsController()


    def test_get_students_smoke(self):

        all_st = self.students_ctrl.get_students()

        with soft_assertions():
            assert_that(len(all_st), 'Number of items in response must be 10').is_equal_to(10)

            # for case of checking each of 10 students
            for st in all_st:
                StAssert.base_check_student(st)


    def test_get_student_smoke(self):

        st = self.students_ctrl.get_student(1, check_schema=False)

        assert_that(st.get('id'), 'student id must be 1').is_equal_to(1)
        StAssert.base_check_student(st)

# pip install pytest-xdist
# pytest -n 4
# https://refactoring.guru/uk