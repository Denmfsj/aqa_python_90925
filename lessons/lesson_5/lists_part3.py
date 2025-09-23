
my_friends = ['Den', 'Alex', 'Yur']

# insert

my_friends.append('Valik')
# print(my_friends)
my_friends.insert(0, 'Alice')
# print(my_friends)
my_friends.insert(2, 'Vik')
# print(my_friends)
my_friends.insert(5555, 'Olga')
print(my_friends)

# pop
my_friends.pop() # видались останній елемент
my_friends.pop() # видались останній елемент

print(my_friends)
my_friends.pop(1)
print(my_friends)
# my_friends.pop(6666)
# my_friends[55]

my_friends.remove('Alex')
# my_friends.remove()  помилка
print(my_friends)
# my_friends.remove('11111')
my_friends.clear()  # очистити список
print(my_friends)