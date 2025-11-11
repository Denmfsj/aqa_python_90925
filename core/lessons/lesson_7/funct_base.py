

# list_of_users = [{'id': 1, 'name': 'Ivan'}, ]
#
#
# def check_user_ids_are_unique():
#     fuser_ids = [k['id'] for k in list_of_users]
#     set_of_isd = set(fuser_ids)
#
#     if len(set_of_isd) != len(fuser_ids):
#         print('Some Ids are not unique')
#
#
# def user_list_is_not_empty():
#     pass


def greetings(name):
    print(f'Hello {name}')


def custom_separator(quan_of_dashes=80):

    print('-'*quan_of_dashes)
    print('New block of code')
    print('-'*quan_of_dashes)


def custom_separator_short(quan_of_dashes=10):

    print('|'*quan_of_dashes)


if __name__ == '__main__':
    greetings('Den')
    custom_separator()
    user_name = 'Alex'
    greetings(user_name)
    custom_separator()
    custom_separator_short()