import json

user_data = (
    {"name": "John", "age": 30, "city": None},
    {"name": "John", "age": 30, "city": True},
    {"name": 'Alex', "age": 30, "city": "New York"},
)

# python_from_json = json.loads(str(user_data))


json_obj = json.dumps(user_data)

with open('user_data.json', 'w') as f:
    json.dump(user_data, f, indent=4)  # запис в файл

with open('user_data.json') as f:
    restored_json_data = json.load(f)  # читання з файла

print(restored_json_data)
print(restored_json_data[0])


# print(user_data)
# print(json_obj)
# print(type(json_obj))
#
# python_from_json = json.loads(json_obj)
# print(python_from_json)
# print(python_from_json[1].get('age'))

