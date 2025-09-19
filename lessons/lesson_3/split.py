

row = 'РозділенняРозділення строки на частини  – split() '

# row_splitted = row.split('о')  # список строк

# print(row_splitted)

row_splitted = row.split(' ')
print(row_splitted)
# print(row.split('Розділення'))

print(row.split())  # ділити по пробілам, але не буде порожні рядків

print(f'в рядку ми маємо {len(row.split())} слів')


import re
рядок = "1apple2orange3banana"
частини = re.split(r'\d', рядок)  # regexp
print(частини)

row = ('Частина 1 Висновок: юююю Частина 2 ... Висновок: .....Розділення строки на частини '
       'Висновок: split() фів фів фів фів фів ')

last_vysn = row.split('Висновок')
print(last_vysn)
print(last_vysn[-1])

# [1,2,34,45,56,76,78,788][-1]
# 'asdad gvasdfg sdf d'[-1]


