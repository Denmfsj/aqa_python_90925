

# def print_greetings():
#
#     name = 'Den'
#     print(f'Hello {name}')
#
#
# name = 'Alex'
# print_greetings()
# print(name)

api_response = [
    {'id': 1, 'name': 'Den'},
    {'id': 2, 'name:':'Ihor'},
    {'id': 4, 'name:':'Nikita'},
]
api_response_2 = [
    {'id': 1, 'name': 'Den'}
]


def validate_users(users):

    def _user_validation():
        """Багато незрозумілих перевірок"""

        print(f'checking user {user}')
        if user['id'] < 1:
            print('Id can be less than 1')

    if len(users) < 2 :
        print('The list must contain at least 2 users')
        return  # return None закінчую виконання Функції

    for user in users:
        print(user)

    _user_validation()


validate_users(api_response)

