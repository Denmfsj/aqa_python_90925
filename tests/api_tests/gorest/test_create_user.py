# http://gorest.co.in/public/v2/users
import requests
from curlify import to_curl
from requests.auth import HTTPDigestAuth, HTTPBasicAuth



def test_create_user():

    url = 'http://gorest.co.in/public/v2/users'

    extra_headers = {'Authorization': "Bearer ea1cf6a5c93238bfcd0c086b790f2353ff4418d899c26f8b9e8906a190c1111e",
                     "User-Agent": 'AQA_TEST_REQUEST'}

    new_user_body = {"name": "Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}

    response = requests.post(url=url, json=new_user_body, headers=extra_headers,
                             auth=HTTPBasicAuth(username='den', password='den'))

    print(to_curl(request=response.request))

    print('response time is', response.elapsed.total_seconds())

    assert response.status_code == 200
    print('headers in response', dict(response.headers))
    print('headers in request', dict(response.request.headers))


