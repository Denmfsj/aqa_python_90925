expected_age = 42

user_age = input('Enter your age: ')  # завжди строка

user_age = int(user_age)  # зробити число зі строки

max_age = max(user_age, expected_age)
min_age = min(user_age, expected_age)

print('Max age is ', max_age)
print('Max age is ', min_age)

# --------------------------------------
list_of_number = [1,2,3,10,6,22]
max_in_list = max(list_of_number)
min_in_list = min(list_of_number)
print(max_in_list)
print(min_in_list)