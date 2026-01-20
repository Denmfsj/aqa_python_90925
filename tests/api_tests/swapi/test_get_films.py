# https://swapi.info/api/films
import requests
import pytest


@pytest.mark.swapi
def test_get_films_smoke():

    url = 'https://swapi.info/api/films'
    response = requests.get(url)

    assert response.status_code == 200, f"Status code for {url} must be 200"

