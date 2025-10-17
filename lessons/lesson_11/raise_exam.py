# try except finally

# assertpy

users = [{'id': None, 'name': 'Alex'}, {'id': 3, 'name': ''}, {'id': 1, 'name': 'Alex'}]


for user in users:

    # assert len(user['name']) != 0, 'User has name = ""'

    if not(type(user['id'])  == int and user['id'] > 0):
        raise AssertionError('User has incorrect id')

    if not(len(user['name']) != 0):
        raise AssertionError('User has name = ""')



