import requests

from core.api.students_service.student_dto import StudentSchema
from utils.settings import d_settings


class StudentsController:

    def __init__(self):
        self.__auth_token = None
        self.base_url = d_settings.STUDENT_URL  # 'http://127.0.0.1:8080'


    def __get_token(self):
        if self.__auth_token is None:
            self.__auth_token = self.get_auth()
        return self.__auth_token

    def get_auth(self):
        return requests.post(url=f'{self.base_url}/auth',
                             json={
                                 'name': d_settings.STUDENT_SERVICE_NAME,
                                   'password': d_settings.STUDENT_SERVICE_PWD
                                   }).text

    def get_students(self, check_schema=True):
        data =  requests.get(url=f'{self.base_url}/students/').json()

        if check_schema:
            StudentSchema(many=True).load(data)  # перевіка відповіді на співставність до схеми

        return data

    def get_student(self, st_id: int, check_schema=True):
        data =  requests.get(url=f'{self.base_url}/students/{st_id}').json()

        if check_schema:
            StudentSchema().load(data)

        return data
