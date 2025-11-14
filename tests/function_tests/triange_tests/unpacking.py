lst_of_data = [1,2,34,54, 'adg,dfh,sd,g']

print(lst_of_data, sep=' ||| ')
print(*lst_of_data, sep=' ||| ') # print(1,2,34,54, 'adg,dfh,sd,g', sep=' ||| ')

def print(*args, sep=' ', end='\n'):
    pass


first, second, *all_others = lst_of_data  # 1, 2, [34,54, 'adg,dfh,sd,g']


class User:

    def __init__(self, name, age, date, sex):
        self.name = name
        self.age = age
        self.date = date
        self.sex = sex


# den = User(name='Den', age=30, date='2025', sex='m')

# den = User(**{'name': 'Den', 'age': 30, ...})#  == User(name='Den', age=30, date='2025', sex='m')