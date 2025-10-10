
class Course:

    def __init__(self, name: str, duration: int, users: list = None):
        self.name = name
        self.duration = duration
        self.users = users

    def __getattr__(self, item):
        return self.__dict__.get(item, f'You dont have this attr {item}')  # якщо є атрибут - віддай значення. Інакше фразу

    def __str__(self):
        return f'{self.name}, duration = {self.duration} months. Students on the course = {self.users}'

math = Course('math', 6, ['Alex', 'Igor'])
lith = Course('lith', 3)

print(math.duration)  # math.__getattr__('duration')  ==> getattr(math, 'duration')
print(math.asd)   # math.__getattr__('asd')  ==> getattr(math, 'asd')

# print(math.name)
# print(math.duration)
#
# math_users = getattr(math, 'users')  # (звідки - змінна, який_атрибут - строка)
# print(math_users)

required_attributes = ['name', 'unknow']


# for k in required_attributes:
#     print(k, getattr(math, k))
#     print('-'*80)