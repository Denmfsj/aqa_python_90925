import unittest
from unittest.mock import patch, Mock

import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self):
        url = f"{self.base_url}/data"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None


class TestAPIClient(unittest.TestCase):

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        # Створюємо макет відповіді API-ендпоінта
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'example_data'}

        # Встановлюємо макет для функції get() з бібліотеки requests
        mock_get.return_value = mock_response

        # Тестуємо метод get_data() з класу APIClient
        api_client = APIClient(base_url='https://api.example.com')
        result = api_client.get_data()

        # Перевіряємо, чи метод get() був викликаний з очікуваним URL
        mock_get.assert_called_once_with('https://api.example.com/data')

        # Перевіряємо результат
        self.assertEqual(result, {'data': 'example_data'})

    @patch('requests.get')
    def test_get_data_failure(self, mock_get):
        # Створюємо макет відповіді API-ендпоінта для
				# симуляції невдачі (status_code != 200)
        mock_response = Mock()
        mock_response.status_code = 404

        # Встановлюємо макет для функції get() з бібліотеки requests
        mock_get.return_value = mock_response

        # Тестуємо метод get_data() з класу APIClient при невдачі
        api_client = APIClient(base_url='https://api.example.com')
        result = api_client.get_data()

        # Перевіряємо, чи метод get() був викликаний з очікуваним URL
        mock_get.assert_called_once_with('https://api.example.com/data')

        # Перевіряємо, що результат - None при невдачі
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()