# list_of_number = [1,2,3,None, 0, 4]

# for number in list_of_number:
#
#     if isinstance(number, int):
#
#         if number != 0:
#             print(10/number)
#         else:
#             print('Cant work with 0')
#     else:
#         print(f'Cant work with {number}')

print('-'*80)

list_of_number = [0, None, 1,2,3,None, 0, 4]

users = [{'years_in_uni': 5, 'classes_of_beer': 30}, {'years_in_uni': 0, 'classes_of_beer': 0},
        {'years_in_uni': None, 'classes_of_beer': 30}, {'classes_of_beer': 30}]

for user in users:
    try:

        print(user['classes_of_beer'] / user['years_in_uni'])

    except (ZeroDivisionError, TypeError):
        print(f'Cant work with {user}')

    except Exception:
        print(f'Smth wrong had happend with {user}')


# for number in list_of_number:
#     try:
#         print(10/number)
#     except ZeroDivisionError:  # ZeroDivisionError -> ArithmeticError -> Exception
#         print('Cant work with 0')
#     except TypeError:   # TypeError -> Exception
#         print(f'Cant work with {number}')
#     except Exception:
#         print(f'Smth wrong had happend with {number}')
