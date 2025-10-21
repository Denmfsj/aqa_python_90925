row = 'Asdf a fdg adf Asdfg asfg asdf'

print('First word')
print('Second word')


print_data = ''

for char in row:  # FOR(для) кожного символа В(in) строці
    print_data = print_data + char
    print(print_data)


splitted_row = row.split()  # розбити по пробілам, буде список
print(splitted_row)

for word in splitted_row:

    if word.istitle():
        print(word, 'is Title!!!')


# print('last time = ', asdasdasdasd)