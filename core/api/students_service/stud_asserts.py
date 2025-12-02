from assertpy import assert_that, soft_assertions

class StAssert:

    @staticmethod
    def base_check_student(student):
        with soft_assertions():
            assert_that(student.get('id'), f'id must be more than 0').is_greater_than(0)