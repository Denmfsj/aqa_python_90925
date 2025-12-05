import requests

from core.api.students_service import StudentRoutes
from core.api.students_service.student_dto import StudentSchema
from utils.settings import d_settings


class StudentsController:

    def __init__(self):
        self.__auth_token = None
        self.base_url = d_settings.STUDENT_URL  # 'http://127.0.0.1:8080'


    def __get_token(self):
        if self.__auth_token is None:
            print('\n\n!---------------------Getting token----------------------!\n\n')
            self.__auth_token = self.get_auth()
        return self.__auth_token

    def get_auth(self):
        return requests.post(url=f'{self.base_url}/auth',
                             json={
                                 'name': d_settings.STUDENT_SERVICE_NAME,
                                 'password': d_settings.STUDENT_SERVICE_PWD
                             }).text

    def get_students(self, check_schema=True, status_code=200):
        response =  requests.get(url=f'{self.base_url}/students/')

        if status_code:
            assert response.status_code == status_code, f'Status code must be {status_code}'

        if check_schema:
            StudentSchema(many=True).load(response.json())  # перевіка відповіді на співставність до схеми


        return response.json()

    def get_student(self, st_id: int, check_schema=True, status_code=200):
        response =  requests.get(url=f'{self.base_url}/students/{st_id}')

        if status_code:
            assert response.status_code == status_code, f'Status code must be {status_code}'

        if check_schema:
            StudentSchema().load(response)


        return response.json()

    def create_student(self, input_params: dict, check_schema=True, status_code=201):
        response = requests.post(url=f'{self.base_url}/students/',
                             json=input_params,
                             headers={'token': self.__get_token()})

        if status_code:
            assert response.status_code == status_code, f'Status code must be {status_code}'

        if check_schema:
            StudentSchema().load(response.json())

        return response.json()

    def update_student(self, st_id: int, input_params: dict, check_schema=True, status_code=200):
        response = requests.put(
            url=f'{self.base_url}/students/{st_id}',
                             json=input_params,
                             headers={'token': self.__get_token()})

        if status_code:
            assert response.status_code == status_code, f'Status code must be {status_code}'

        if check_schema:
            StudentSchema().load(response.json())

        return response.json()

    def delete_student(self, st_id: int, status_code=204):
        response = requests.delete(url=f'{self.base_url}/students/{st_id}',
                             headers={'token': self.__get_token()})

        if status_code:
            assert response.status_code == status_code, f'Status code must be {status_code}'
