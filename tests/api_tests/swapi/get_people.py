import requests
import pytest
from assertpy import soft_assertions, assert_that



people_url = 'https://swapi.dev/api/people'

@pytest.mark.swapi
def test_get_people_smoke():

    response = requests.get(people_url)

    assert response.status_code == 200, f"Status code for {people_url} must be 200"

@pytest.mark.swapi
@pytest.mark.parametrize('search_phrase', ['re', 'a', 'ololo'])
def test_get_people_search(search_phrase):

    qp = {'search': search_phrase}

    response = requests.get(people_url, params=qp)
    print(response.url)

    assert response.status_code == 200, f"Status code for {people_url} + {qp} must be 200"
    people = response.json().get('results')

    with soft_assertions():
        for person in people:
            print(f'checking {person.get("name")}')
            assert_that(search_phrase).is_in(person.get('name'))

@pytest.mark.swapi
def test_get_people_base_people_data():


    response = requests.get(people_url)
    print(response.url)

    assert response.status_code == 200, f"Status code for {people_url} must be 200"
    people = response.json().get('results')

    with soft_assertions():
        for person in people:
            print(f'checking {person.get("name")}')

            height = int(person.get('height'))
            len_of_name = len(person.get('name'))

            base_message = f'person={person.get("name")}, checkin'

            base_message  += ', checking {}'

            assert_that(len_of_name, base_message.format('name len')).is_greater_than(20)
            assert_that(height, base_message.format('height')).is_greater_than(150)

            person_page_status = requests.get(person.get('url')).status_code
            assert_that(person_page_status, base_message.format('personal page')).is_equal_to(200)

            for film_url in person.get('films'):
                film_status = requests.get(film_url).status_code
                assert_that(film_status, base_message.format(f'Films {film_url}')).is_equal_to(200)







#
# @pytest.mark.parametrize('search_phrase', ['re', 'a', 'ololo'])
# def test_get_people_search_2(search_phrase):
#
#     qp = {'search': search_phrase}
#
#     response = requests.get(people_url, params=qp)
#     print(response.url)
#
#     assert response.status_code == 200, f"Status code for {people_url} + {qp} must be 200"
#     people = response.json().get('results')
#
#     for person in people:
#         print(f'checking {person.get("name")}')
#
#         assert '123' in person.get('name'), \
#             f'{search_phrase} must be in name, user name = {person.get("name")}'
