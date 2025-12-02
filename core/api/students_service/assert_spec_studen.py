from core.api.students_service.stud_asserts import StAssert


class AssertSpecificStudent(StAssert):

    def check_student_332(self, stud):
        self.base_check_student(stud)

        assert stud.get('id') == 332