
# +       -       *       **      /       //      %

age = 42
new_age = 18

# print(age + new_age)
# print(age - new_age)
# print(2**5)
# print(2**3)

res1 =  12/6  # звичайне ділення, повертає float == 2.0
res2 =  12//6  # звичайне ділення, повертає int == 2
res3 =  12/5  # звичайне ділення, повертає float == 2.4
res4 =  12//5  # звичайне ділення, повертає int == 2

# print('12/6 => ', res1)
# print('12//6 => ', res2)
# print('12/5 => ', res3)
# print('12//5 => ', res4)
# print('-5.9//1 => ', (-5.9)//1)
# print('5.9//1 => ', 5.9//1)

# print('12%5  => ', 12%5)  # 12 / 5 = 5 + 5 + 2 => 2

# print(2311234123123 % 2)
# print(2311234123122 % 2)



# print('v1 Your age is', 22 + 33)
# print('v2 Your name is', name := input('Enter your name: '))

# print('Yes, your name is', name)


# <       >       <=      >=      ==      !=

my_age_more_10  = 32 > 10  # True
my_age_less_12  = 32 < 12  # False
my_age_is_equal_to_32  = 32 == 32  # True
my_age_is_less_equal_to_31  = 32 <= 31  # False
my_age_is_more_equal_to_37  = 32 <= 37  # True
my_age_is_not_100  = 32 != 100  # True

wrong_data = [1,23]
print('Do we have wrong data: ', len(wrong_data) != 0)

name = 'Denys'  # len(name)  = 5
tuple = (1,2,3)  # len(tuple)  = 3
print('tuple', len(tuple))
list_obj = [1,2,3]
dict_obj = {'Name': 'Alex', 'age': 44}
set_obj = {1,23,455}
print('dict_obj', len(dict_obj))

data = None
is_have_job = True
age = 23
temp = 4.44

name_in_dct = dict_obj['Name']

name2 = dict_obj.get('Name')

print(name_in_dct)
print(name2)


# ---------------- Float -------------------
total_price = 0.3
first_item = 0.2
second_item = 0.1


expected_price = second_item + first_item
print(expected_price)
print('expected_price == total_price', expected_price == total_price)

# округлення
expected_price = round(second_item + first_item, 2)  # окреглення до другго знака(бо 2 другий аргумент)
# round(0.123, 2) = 0.12
# round(0.166666, 3) = 0.167
# працює по правила банківськго окреглення
# 0.55 => 0.5, 0.65 => 0.7
print(expected_price)
print('expected_price == total_price', expected_price == total_price)


