import random
from assertpy import soft_assertions, assert_that

# from core.api.students_service.db.student_all_tabnle import StudentsTable
from core.api.students_service.stud_asserts import StAssert


class TestCreateStudents:


    def test_create_student(self, stud_ctrl, random_student_name):

        student_name = random_student_name
        student_score = random.choice(range(50,100))

        response_json = stud_ctrl.create_student(
            {
                'name': student_name,
                'score': student_score
            }
        )

        StAssert.base_check_student(response_json)

        with soft_assertions():

            assert_that(student_name,
                        f'Name must be {student_name}').is_equal_to(response_json.get('name'))
            assert_that(student_score,
                        f'score must be {student_score}').is_equal_to(response_json.get('score'))



        # db_data = StudentsTable().get_student_by_id(response_json.get('id'))
        # with soft_assertions():
        #
        #     assert_that(student_name,
        #                 f'Name must be {student_name}').is_equal_to(db_data.get('name'))
        #     assert_that(student_score,
        #                 f'score must be {student_score}').is_equal_to(db_data.get('score'))

