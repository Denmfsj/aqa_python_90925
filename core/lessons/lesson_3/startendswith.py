row = 'етоди .startswith() та .endswith() використовуються для перевірки т'

print(row.startswith('етоди .'))  # True
print(row.startswith('е'))  # True
print(row.startswith('етоди s'))  # False

print(row.endswith('ревірки т'))  # True
print(row.endswith(' т'))  # True
print(row.endswith('ревірки  т'))  # False

