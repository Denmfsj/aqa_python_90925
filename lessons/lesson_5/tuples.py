my_tuple = (1,2)

tuple_of_ages = (22,33,444)
tuple_of_names = ('den', 'alex')
tuple_of_tuples = ((1,2), ('a', 'b'))

# print(type(tuple_of_ages), tuple_of_ages)
# print(type(tuple_of_names), tuple_of_names)
# print(type(tuple_of_tuples), tuple_of_tuples)

my_tuple = ('a', 'den', 3.14, None, False, tuple_of_ages)

names = ('Den')  # str
names = ('Den',)  # tuple
ages = 33,5  # tuple
# print(names, type(names))
# print(ages, type(ages))

my_name = 'Denys'
my_name_tuple = tuple(my_name)  # ('D', 'e', 'n', 'y', 's')
# print(my_name_tuple)


# print(my_name_tuple[2])
# print(my_name_tuple[1:])

number = (1,4,5,1,6,'den', 3.14)

# print(number[-2])  # den
before_lase_element = number[-2]  # строка den
last_symb_in_row = before_lase_element[-1]  # строка n
# print(number[-2][-1]) # == last_symb_in_row,  n
# print(number[1])

#print('aaaabcd'.count('a'))
#print(number.count(1))
#print(number.count('den'))
#print(number.count('1'))

# print(number.index(4))  # index=1
# print(number.index('den'))  # index=5
# print(number.index(1, 2))  # index=3

tuple_of_lists = ([1,2], ['Den', 'Alex'])

print(tuple_of_lists, id(tuple_of_lists))

last_el = tuple_of_lists[-1]
last_el.append('Yur')
print(tuple_of_lists, id(tuple_of_lists))
MAX_AGE_IN_SYSTEM = 99  # constant
