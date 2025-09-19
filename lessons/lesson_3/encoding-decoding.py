

greetings = 'Привіт'  # utf-8

# greetings_win_1251 = greetings.encode('windows-1251')
greetings_win_1251 = b'\xcf\xf0\xe8\xe2\xb3\xf2'  # windows-1251
print(greetings)
print(greetings_win_1251)

greetings_utf_8 = greetings_win_1251.decode('windows-1251')
print(greetings_utf_8)