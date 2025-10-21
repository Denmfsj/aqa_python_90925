
my_friends = ['Den', 'Alex', 'Yur']
print(id(my_friends))
my_friends.append([1,2])

print(my_friends)
print(id(my_friends))
my_friends.extend([3,4])  # додає кожний елемент окремо в кінець списку
# my_friends.append(3) my_friends.append(4)
print(id(my_friends))
print(my_friends)

print(id(my_friends))
my_friends = my_friends + [5,6]  # ми створили змінну
print(id(my_friends))
print(my_friends)
new_list = [1,2,3] + ['a', 'b', 'c']  # створю новий список [1, 2, 3, 'a', 'b', 'c']
# print(new_list)
# print(my_friends)


