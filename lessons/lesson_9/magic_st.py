


class ApiUser:
    def __init__(self, id, name, age, scopes):
        self.id = id
        self.name = name
        self.age = age
        self.scopes = scopes

    def __str__(self):
        return f'class: ApiUser, id={self.id}, name={self.name}'

    def print_user_info(self):
        print(f'id={self.id}, name={self.name}')


person = ApiUser(1, "John", 25, ['read-all'])
print(person)  # print(str(person))
print(str(person))
print(person.__str__())
