card_number = 11223344
cvv = 1231
has_money = False
zero_on_account = True # нем коштів

# якщо я знаю номер + cvv   + є гроші, то
# if bool((card_number == 11223344) and (cvv == 123) and (zero_on_account is False)):
# if True and True and True:

# if (card_number == 11223344) and (cvv == 123) and has_money:
#     print('You can send money')
#
# elif not has_money:
#     print('You have no money')
#
# elif cvv != 123:
#     print('You put incorrect cvv')
#
# else:
#     print('Smth went wrong')
#
# print('Done')

# test_type = 'Full check'
test_type = 'smoke check'
list_of_users = []


    # isinstance(list_of_users, list) == type(list_of_users) is list
if not isinstance(list_of_users, list):  # чи є list_of_users списком, поверне True or False
    print('Error: not a list')

if test_type == 'Full check':
   if not list_of_users:
       print('list_of_users must be not empty')






# list_of_users = [
#     {'id': 1, 'has_score': True},
#     {'id': 2, 'has_score': False}
# ]
#
# for user in list_of_users:
#
#     if user['has_score']:
#         ...
#     else:
#         print('Error ')