
class AgeError(Exception):

    def __init__(self, age):
        message = f'You are not allow to do this action in your {age}'
        super().__init__(message)




user_age = int(input('Set your name: '))

if 18 < user_age < 60:
    raise AgeError(user_age)