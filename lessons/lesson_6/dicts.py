

my_details = {'hobby': 'puzzle',
              'swimming': True}

my_info = {

    # 1 + 2: 2,
    # 55.5: 'asd',
    # None: 123,
    # False: 123,
    # list, set, dict не можуть бути ключами


    'id': 1,
    'name': 'Den',

    'info': {
        'position': 'AQA',
        'skills': ['Python', 'Git'],
        'var': None
    },
    'extra_details': my_details,
}

# for k in my_info:
#     print(k, my_info[k])

# for k in my_info.keys():
#     print(k, my_info[k])

# for k in my_info.values():
#     print(k)

# for key, value in my_info.items():
#     print('key:', key)
#     print('val:', value)
#     print('-'*80)

my_info.items()


list_from_dict_items = list(my_info.items())
print(list_from_dict_items)

# for k, v in my_info.items():  # [('id', 1), ('name', 'Den'), ('info', {'position': 'AQA', 'skills': ['Python', 'Git'], 'var': None}), ('extra_details', {'hobby': 'puzzle', 'swimming': True})]

# for key, value in [('key1', 'value1'),('key2', 'value2'),('key3', 'value3')]:
#     print('key:', key)
#     print('val:', value)
#     print('-'*80)

for key in [('key1', 'value1'),('key2', 'value2', 'smth_new'),('key3', 'value3')]:
    print('key:', key)
    # print('val:', value)
    print('-'*80)


# user_id = my_info['id']  # небезпечний доступ
# user_name = my_info.get('name', 'Alex')  # безпечний доступ
# print(f'user_id = {user_id}')
# print(f'user_name = {user_name}')


