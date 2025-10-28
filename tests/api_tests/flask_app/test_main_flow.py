import requests
import pytest

from definitions import READ_WRITE_TEMP_FILE



base_url = 'http://127.0.0.1:7070'

content = {'cars': ['Audi, VW', 'Toyota']}
updated_content = {'bikes': ['Honda', 'Suzuki']}


@pytest.mark.flask_local_app
class TestContent:


    @pytest.fixture  # спец слово для використання в тестах
    def create_content(self):

        # Записувати іякісь дані в файл
        with open(READ_WRITE_TEMP_FILE, 'w') as f:
            f.write(';some etxt')

        response_data = requests.post(f'{base_url}/content', json=content)
        id_of_created_content = response_data.json()['id']
        print(f'precondition content was created, {id_of_created_content}')

        yield id_of_created_content  # return from precondition

        # postcondition
        url_for_delete = f'{base_url}/content/{id_of_created_content}'
        requests.delete(url_for_delete)
        print(f'precondition content was deleted, {id_of_created_content}')



    def test_add_content(self):
        response_data = requests.post(f'{base_url}/content', json=content)
        assert response_data.status_code == 200, "Content was not created"
        assert response_data.json().get('id') == 'Content created successfully!'


    def test_get_content(self, create_content):

        # чситати файл
        with open(READ_WRITE_TEMP_FILE) as f:
            data_file = f.read()

        response_get = requests.get(f'{base_url}/content')
        assert response_get.status_code == 200, "Unable to get content"
        server_content = response_get.json().get('content')
        assert content in server_content


    def test_modify_content(self, create_content):
        response = requests.put(f'{base_url}/content/{create_content}', json=updated_content)
        assert response.status_code == 200, "Unable modify content"
        assert response.json().get('message') == 'Content updated successfully!'


    def test_deleting_content(self, create_content):
        response = requests.delete(f'{base_url}/content/{create_content}')
        assert response.status_code == 200, "Unable delete content"
        assert response.json().get('message') == 'Content deleted successfully!'

