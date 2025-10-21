users = [
    {'id': 1, 'name': 'Den', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 2, 'name': 'Alex', 'age': 30},
    {'id': 3, 'name': 'Igor', 'age': 40, 'job': None},
    {'id': 4, 'name': 'Ivan', 'age': 50, 'job': [{'id': 2, 'title': 'CEO'}]},
    {'id': 5, 'name': 'Mor', 'age': 60, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 6, 'name': 'Viktor', 'age': 70, 'job': [{'id': 3, 'title': 'Retired'}]},
    {'id': 7, 'name': 'Maria', 'age': 20, 'job': [{'id': 1, 'title': 'QA'}]},
    {'id': 8, 'name': 'Anna', 'age': 20, 'job': []},
    {'id': 9, 'name': 'Inna', 'job': [{'id': 1, 'title': 'QA'}]},
]

# вік від 0 до  60 - ok, інакше - не друкувати
# всі повинні мати job, якщо нема то  не друкувати
# друкувати user_id
#
# for user in users:
#
#
#     if  user.get('age', 999) >= 60 :
#         continue  #  перейли до наступного елементу цикла в початок
#
#     if  user.get('age', 999) < 0:
#         continue
#
#     if not user.get('job'):
#         continue
#
#     # if  (user.get('age', 999) >= 60) or (not user.get('job')):
#     #     continue
#
#
#     print(user.get('id'), 'Valid')


list_of_numbers = [1,0,5,0, 8]

for number in list_of_numbers:

    if number == 0:
        # print('cant divide by zero')
        continue

    print(10/number)
else:
    print('WE have no break')

print('-'*80)


for number in list_of_numbers:

    if number == 0:
        break  # розриває икл і виходить з нього

    print(10/number)
else:
    print('WE have no break')
print('Done')