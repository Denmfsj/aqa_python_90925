

my_positive_list = [1, 'asd', True]  # bool(1) -> True,  bool(asd) - > True
my_not_positive_list = [0, 'asd', True]  # bool(0) -> False,  bool(asd) - > True
res_1 = all(my_positive_list)  # чи всі  True
res_2 = all(my_not_positive_list)


any_1 = any(my_positive_list)  # чи хоча 1  True
any_2 = any(my_not_positive_list)
#
#
# print(any_1)
# print(any_2)

list_of_user = [
    {'second_name': 'Al', 'name': 'Alex', 'age': 20},
    {'second_name': 'S', 'name': 'Olga', 'age': 10},
    {'second_name': 'X', 'name': '', 'age': 30},
    {'second_name': 'S', 'name': 'Olga', 'age': 50},
    {'second_name': 'T', 'name': '', 'age': 17},
]


def filter_by_age(user_data):

    return user_data.get('age', 0) >= 18  # True or False

    # if user_data.get('age', 0) >= 18:
    #     return True
    # else:
    #     return False

filtered_list = list(filter(filter_by_age, list_of_user))
filtered_list2 = list(filter(lambda x: x.get('age', 0) >= 18, list_of_user))
filtered_list3 = [k for k in list_of_user if filter_by_age(k)]

list_of_numbers = range(10, 20)  # [10,11,12,13,14,15,16,17,18,19]
list_of_second_numbers_v1 = range(5, 7)  # [5, 6]
list_of_second_numbers_v2 = range(5, 100)  # [5,6,7,8,9,10,11,12,...,99]

def raise_in_number(original, st):
    return original ** st

list_of_sq_v1 = list(map(raise_in_number, list_of_numbers, list_of_second_numbers_v1))
list_of_sq_v2 = list(map(raise_in_number, list_of_numbers, list_of_second_numbers_v2))
#
print(list_of_sq_v1)
# print(list_of_sq_v2)


min_of_numbers = min([1,5,4,5,0,-5,6])
max_of_numbers = max([1,5,4,5,0,-5,6])
print(min_of_numbers)
print(max_of_numbers)

print(sum({1,2,3,4,555,7,8,}))

print(round(2.61111, 3))  # 2.611
print(round(2.61111, 0))  # 3.0

#
# print(filtered_list)
# print(filtered_list2)
# print(filtered_list3)



# filtered_list = []
# for user in list_of_user:
#     if user['age'] >= 18:
#         filtered_list.append(user)

# for user_index, user in enumerate(list_of_user):
#
#     if user['name'] == '':
#         print(f'User with index = {user_index} adn second name = {user["second_name"]} has empty name')



# max, min