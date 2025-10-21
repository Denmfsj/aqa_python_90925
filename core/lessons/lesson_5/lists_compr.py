
phrase = 'Hey my name is Denys!'
list_of_chars = []

for char in phrase:
    # print(char)
    if char != ' ': # додаватиа якщо символ не пробіл
        list_of_chars.append(char)

# print(list_of_chars)

# list_comprehension = [char for char in phrase if char != ' ']
# for char in phrase:
    # print(char)
#     list_of_chars.append(char)

# print(list_of_chars)

# list_comprehension = [char for char in phrase]

# [змінна_яку_додаю_в_новий_список for змінна_яку_додаю_в_новий_список in щось if умова]
# print(list_comprehension)


# ---------------------------
user_data = [
    (1, 90),
    (2, 55),
    (10, 94),
    (11, 94),
    (13, None),
    (6, 77)
]

# кількість юзерів зі скором більше 60

prepare_count_of_users = [1 for k in user_data if k[1] is None and k[1] > 60 ]
count_of_users = sum(prepare_count_of_users)
print(prepare_count_of_users)
print(count_of_users)


# for user in user_data:
# if user[1] != None:
#         assert 100 > user[1] > 0, f'User with id {user[0]} has incorrect score = {user[1]}'

# filtered_user_data = [k for k in user_data if k[1] != None]

# for user in filtered_user_data:
#     assert 100 > user[1] > 0, f'User with id {user[0]} has incorrect score = {user[1]}'

# sorted_score_user_data = sorted(user_data, key=lambda x: x[1])
# print(sorted_score_user_data)