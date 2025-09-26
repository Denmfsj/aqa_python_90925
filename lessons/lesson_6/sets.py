

num_1 = 5
num_2 = 10
# print(num_1, num_2)


# print(list_of_friends)
# temp = None
#
# temp = num_1
# num_1 = num_2
# num_2 = temp
#
# print(num_1, num_2)

num_1, num_2 = num_2, num_1
# print(num_1, num_2)

# list_of_friends = ['Alex', 'Nora', 'Ali']
#
# list_of_friends[0], list_of_friends[1] = list_of_friends[1], list_of_friends[0]

# ------------------------------


# set_of_friends = {'Alex', 'Nora', 'Ali', 'Alex'}  # {1,2,3} - set
#
# print(set_of_friends)
#
# ali_in_set = 'Ali' in set_of_friends  # True
# lisa_in_set = 'Lisa' in set_of_friends  # False
# print(ali_in_set)
# print(lisa_in_set)
#
# list_of_ids = [1,2,3,4,5,5]
# set_of_user_ids = set(list_of_ids)
#
# print('list_of_ids', list_of_ids)
# print('set_of_user_ids', set_of_user_ids)
# list_from_set = list(set_of_user_ids)
# print(list_from_set)
# do_we_have_duplicates = len(list_of_ids) == len(set_of_user_ids)  # оскільки довжина елементів різна 6 == 5  ==> False
#
#
# # f'do we have duplicates: {not False}'   ==> f'do we have duplicates: {True}'
# print(f'do we have duplicates: {not do_we_have_duplicates}' )
# ---------------------------------------------------------------

set_of_friends = {'Alex', 'Nora', 'Ali', 'Alex'}

# print(set_of_friends, '- Original')
#
# set_of_friends.add('Yuri')  # додаємо 1 значення
# set_of_friends.add('Nora')
# print(set_of_friends)

# set_of_friends = set_of_friends.union([1,2,3])  # додаємо колекію значень створює новий
# set_of_friends = set_of_friends.union({'s1', 's2'})  # додаємо колекію значень створює новий
# set_of_friends = set_of_friends.union(('t1', 't2'))  # додаємо колекію значень створює новий
# set_of_friends = set_of_friends.union('some row')  # додаємо колекію значень створює новий

# print(set_of_friends)

# ------------------------

set_of_friends = {'Alex', 'Nora', 'Ali', 'Alex'}

set_of_enemies = {'Alla', 'Nora', 'Bart'}

# unknown = set_of_friends.intersection(set_of_enemies)
# # print(unknown)
#
# some_names = ['Alex', 'Nora', 'Marge']
# print(set_of_friends.difference(some_names), 'Тільки в set_of_friends')
# print(set(some_names).difference(set_of_friends), 'Тільки в some_names')
#
# print(set(some_names).symmetric_difference(set_of_friends), 'Тільки в some_names АБО в set_of_friends')


# ----------------
# print(set_of_friends)
# name = set_of_friends.pop()
# print(set_of_friends)
# print(name)

# set_of_friends.remove('Nora')
# print(set_of_friends)


# for element in set_of_friends:
#     print(element)

my_set = {1,'asd', 12.1, None, False, True, ('t1', 't2')}

# print(my_set)
print(hash(5445401723082100449))
print(hash(112313123.5))
print(hash('Den'))
print(hash('Den'))
print(hash('Den'))

