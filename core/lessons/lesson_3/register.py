

row = 'Регістр Cимволів строки, перевірка і перетворення регістру '

lower_case = row.lower()  # всі букви будуть малі
upper_case = row.upper()  # всі букви будуть ВЕЛИКІ
capital_case = row.capitalize()  # перша буква велика, інші малі
title_case = row.title()  # кожне словов починаеться з великаої літери


print(row)
print(lower_case)
print(upper_case)

print(capital_case)
print(title_case)

name = 'Denys Merezhkin'

if name != name.title(): #  'Denys merezhkin' ==  'Denys merezhkin'.title() => 'Denys Merezhkin'
    # raise ValueError('Name of last name is incorrect')
    print('Name of last name is incorrect')


paragraph = 'bal0-bUsdla USD bla-bla'  # usd, USD, Usd

if ' USD ' not in paragraph.upper():
    print('Cant find usd in the paragraph')


print('name.isupper() => ', 'name'.isupper())
print('name.islower() => ', 'name'.islower())
print('Name.istitle() => ', 'Name'.istitle())

print('1'.isdigit())
print('error'.isdigit())

price = 'error!!!'

if price.isdigit() == False:
    print(f'Cant parse prince into number: Price={price}')


# assert price.isdigit(), f'Cant parse prince into number: Price={price}'
