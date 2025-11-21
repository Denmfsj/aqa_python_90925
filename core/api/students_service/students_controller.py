import requests


class StudentsController:

    def __init__(self):
        self.auth_token = None
        self.base_url = 'http://127.0.0.1:8080'


    def get_students(self):
        return requests.get(url=f'{self.base_url}/students/').json()

    def get_student(self, st_id: int):
        return requests.get(url=f'{self.base_url}/students/{st_id}').json()

    def get_auth(self):
        return requests.post(url=f'{self.base_url}/auth',
                             json={'name': 'test', 'password': 'test'}).text

    def create_student(self, input_params: dict):

        return requests.post(url=f'{self.base_url}/students/', json=input_params).json()