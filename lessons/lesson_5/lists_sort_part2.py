my_list = ['Den', 'Alex', 'Ivan', 'Alice', '1', '%$%']

print(my_list)
my_list.sort()  # A, B, C, .., Z, a, b, c, ..., '1', .., '%'
# print(my_list)
my_list.sort(reverse=True)  # '%', '0', '9', ...,  z, y, x, ...a, Z, Y, X, ..., A
# print(my_list)

# відсортувати по довжині імені

# len(k)  - довжина к

# lambda x: len(x)
# lambda  - кключове слово
# lambda x: - для кокжного елемента в списку, це елемент ми записуємо в змінну х\
# lambda x: len(x), len(x) - визначає довжину x, тобто довжину ккожного слова
# на виході у нас список із довжин слів
# ['Den', 'Alex', 'Ivan', 'Alice', '1', '%$%'] => [3, 4, 5, 6, 1, 3]
# ми сортуємо [3, 4, 5, 6, 1, 3]

my_list = ['Den', 'Alex', 'Ivan', 'Alice', '1', '%$%']
new_list = []
for x in my_list:
    print('x', x)
    print('len(x)', len(x))
    new_list.append(len(x))
    print(new_list)
    print('*'*8)

print('Done')
print(new_list)
# [3, 4, 5, 6, 1, 3]
# ['Den', 'Alex', 'Ivan', 'Alice', '1', '%$%']

my_list.sort(key=lambda x: len(x)) # від найкоротшого до найдовшого слова
print(my_list)
# my_list.sort(key=lambda x: len(x), reverse=True) # від найдовшого до найкоротшого слова
# print(my_list)



# print('Den' < 'Alex')  # False
# print('Den' > 'Alex')  # True
# print('K' < 'a')   # True