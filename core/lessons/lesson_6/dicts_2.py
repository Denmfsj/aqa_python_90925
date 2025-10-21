

my_details = {'hobby': 'puzzle',
              'swimming': True}

my_info = {

    'id': 1,
    'name': 'Den',

    'info': {
        'position': 'AQA',
        'skills': ['Python', 'Git'],
        'var': None
    },
    'extra_details': my_details,
}

# user_skills = my_info.get('info', {}).get('skills')  # ['Python', 'Git']
# print(user_skills)
#
# user_skills.append('Oracle')
# # print(my_info['info'])
#
# number_of_skills = len(my_info.get('info', {}).get('skills', []))  #
#
# my_info['quantity_of_skills'] = number_of_skills  # тут я додаю АБО переписую значення quantity_of_skills для my_info
#
# print(my_info)
# my_info['quantity_of_skills'] = 'too much'  # перезапишу
# print(my_info)
#
# deleted_item = my_info.pop('extra_details')
# print(my_info)
# print(deleted_item)
#
# deleted_item = my_info.popitem()
# print(my_info)
# print(deleted_item)
#
#
#
# print('name' in my_info)  # True
# print('Den' in my_info)  # False
# print('position' in my_info)  # False
# print('position' in my_info['info'])  # True

# my_info.clear()



# my_new_dict_with_info = my_info.copy()
import copy
my_new_dict_with_info = copy.deepcopy(my_info)

print(id(my_info), my_info)
print(id(my_new_dict_with_info), my_new_dict_with_info)

my_info['id'] = 2
my_info['info']['skills'].append('Oracle')  # додати 1 елемент до списку skills
my_new_dict_with_info['info']['skills'].append('MSSQL')  # додати 1 елемент до списку skills

print(id(my_info), my_info)
print(id(my_new_dict_with_info), my_new_dict_with_info)




# info_sub_dict = my_info['info']
# print(info_sub_dict)
# skills = info_sub_dict['skills']
# print(skills)
# last_skill = skills[-1]
# print(last_skill)

