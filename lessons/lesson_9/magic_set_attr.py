
class Course:

    def __init__(self, name: str, duration: int, users: list = None):

        self.name = name  # self.__setattr__('name', name)
        self.duration = duration
        self.users = users

    def __setattr__(self, key, value):

        if key == 'name':
            if not(type(value) is str and len(value) > 0):
               print(f'Name must be str and not empty. name={value}')
            else:
                super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)  # метод батька який я не міняв і він просто працює як завжди

    def __str__(self):
        return f'name={self.name}, duration = {self.duration} months. Students on the course = {self.users}'

math = Course('math', 6, ['Alex', 'Igor'])

print(math)
math.name = '' # math.__setattr__(key='name', value='')
print(math)



