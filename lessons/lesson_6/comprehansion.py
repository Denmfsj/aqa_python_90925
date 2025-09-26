
list_of_squares = []

for number in range(10):
    if number%2 == 0:  # якщо парне число
        list_of_squares.append(number**2)

print(list_of_squares)

list_of_squares_v2 = [number**2 for number in range(10) if number%2 == 0]
print(list_of_squares_v2)

set_of_sq = {number**2 for number in range(10) if number%2 == 0}
print(set_of_sq)

list_of_users_hobbies = ['gaming', 'swimming', None, 'gaming']

set_of_hobbies = {k for k in list_of_users_hobbies if k is not None}
print(set_of_hobbies)