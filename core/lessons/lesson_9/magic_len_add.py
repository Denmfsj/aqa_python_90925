import copy


class Course:

    def __init__(self, name: str, duration: int, users: list):
        self.name = name
        self.duration = duration
        self.users = users

    def __len__(self):
        # return self.duration # Довжина курсу =  duration
        return len(self.users) # Довжина курсу =  кільккість студентів

    def __add__(self, secont_option):   # math.__add__(other)

        new_users = copy.copy(self.users)
        new_users.extend(secont_option.users)

        new = Course(
            name=f'{self.name}-{secont_option.name}',
            duration=self.duration + secont_option.duration,
            users=list(set(new_users))
        )

        return new

    def __str__(self):
        return f'{self.name}, duration = {self.duration} months. Students on the course = {self.users}'

math = Course('math', 6, ['Alex', 'Igor'])
lith = Course('lith', 9, ['Inna', 'Alex'])
math_lith = math + lith

math.duration = 12
print(len(math))  # math.__len__()  --> math.users.__len__()
 # math.__add__(lith)

print(math_lith)
print(math)
