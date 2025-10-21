
lst = ["apple", "orange", "banana"]

row = '|'.join(lst)  #  => apple|orange|banana

print(row)

# users?type_id=1,2,3

query_params = ['1','2','3']
separator = '<--->'

url = 'http..../user?type_id='
params = separator.join(query_params)

print(url + params)

# [a, b, c, d, g]  => a b|c|c|d|g

list_of_chars = ['a', 'b', 'c', 'd', 'g']


first_part = list_of_chars[0] + ' '
second_part = '|'.join(list_of_chars[1:])  # list_of_chars[1:] = ['b', 'c', 'd', 'g']

final = first_part + second_part
print(final)
