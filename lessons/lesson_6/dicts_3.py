

list_of_names = ['Alex', 'den', 'ivan', 'ALice']

set_of_len_of_names = {}

for name in list_of_names:
    len_of_name = len(name)

    # якщо len_of_name нема в словнику, то додай до словника len_of_name: []
    set_of_len_of_names.setdefault(len_of_name, [])
    if len_of_name not in set_of_len_of_names:
        set_of_len_of_names[len_of_name] = []


    set_of_len_of_names[len_of_name].append(name)

for k in set_of_len_of_names:
    print(k, set_of_len_of_names[k])


new_dict = dict([(1,2), (3,4)])  # список таплів по 2 елементи, [(key1, value1), (key2, value2), ...]
print(new_dict)