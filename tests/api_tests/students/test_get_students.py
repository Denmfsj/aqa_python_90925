from core.api.students_service.students_controller import StudentsController


class TestGetStudents:

    students_ctrl = StudentsController()


    def test_get_students_smoke(self):

        all_st = self.students_ctrl.get_students()

        assert len(all_st) == 10, 'By default server must return 10 records'


    def test_get_student_smoke(self):

        st = self.students_ctrl.get_student(1)

        assert st.get('id') == 1, 'student id must be 1'


