import math

print('Hello\nworld!')

hello = 'Hello'
world = 'world'
if True:
    print(f"{hello} {world}!")


for letter in 'Hello world!':
    print(letter, end=' ')
print()
apples = 2
banana = apples * 4
print(banana)
apples = 10
print(banana)


# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery =  + side_1 + side_2 + side_3 + side_4
print(perimetery)
print()

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
garden_library = {'Яблуні': 0, 'Груші': 5, 'Сливи':-2 }
print('У саду було посаджено дерев:')
for key, value in garden_library.items():
    garden_library[key]= value+apple_trees
    print(f'{key} = {value+apple_trees}')

print('Bсього дерев = ', sum(garden_library.values()))
print()
print()

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
initial_temp=0;
day_times = {'Ранкова температура': 5, 'Денна темепература': -10, 'Вечірня температурв': 4}
for key, value in day_times.items():
    initial_temp = initial_temp + value
    print(f'{key} = {initial_temp} градусів')
print()

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_number = 24
def children_number(boys, girls):
    return boys+girls
print('Кількість дітей в гуртку сьогодні', children_number(boys_number-1, boys_number//2-2))
print()

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_price = 8
currency = 'грн.'
book_prices = [first_book_price, first_book_price+2, (2*first_book_price+2)//2]
for i, book_price in enumerate(book_prices):
    print(f'Вартість книги №{i+1} = {book_price} {currency}')
print('Загальна вартість книг =', sum(book_prices),currency)