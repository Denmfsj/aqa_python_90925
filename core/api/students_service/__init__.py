class StudentRoutes:


    UPDATE_STUDENT = '/students/{student_id}'


    def path(self, **kwargs):

        return self.UPDATE_STUDENT.format(kwargs)