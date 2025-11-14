lst = [1,2,3]
name = 'den'
info = {'id': 1, 'name': "Alex"}

for k in name:
    print(k)

print('-----')

lst = [1,2,3]
first_iter = iter(lst)
second_iter = iter(lst)

print(next(first_iter))  # first_iter віддав перший елемент
print(next(first_iter))  # first_iter віддав другий елемент
print(next(second_iter))  # second_iter віддав перший елемент


iter_row = iter(name)  # отримали щось, що вміє віддавати елементи послідовно
while True:
    try:
        k = next(iter_row)  # записали в k елемент d
        print(k)
    except StopIteration:  # виникає коли я намагаюсь взяти елемент який ен існує
        break


        k = next(iter_row)  # записали в k елемент e
        print(k)
        k = next(iter_row)  # записали в k елемент n
        print(k)
        k = next(iter_row)  # запитали неіснуючий елемент
        print(k)