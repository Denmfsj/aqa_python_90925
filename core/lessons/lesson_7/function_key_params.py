

def print_description_of_user(user_name: str, nickname: str=None,
                              age: int=None, gender:str =None) -> str:
    """
    Function for printing data aobut user accordint to parameters.
    Also thisi fundtion return as a string this info

    :param user_name: name of user, string
    :param nickname: str
    :param age: This variable is needed for checking if ....
    :param gender:
    :return:
    """


    base_row = f'This is {user_name}'

    if nickname is not None:
        base_row = f"{base_row}, a.k.a. {nickname}."
    if gender is not None:
        base_row = f'{base_row} Gender is {gender}.'
    if age is not None:
        base_row = f'{base_row} {age} years old'

    print(base_row)

    return base_row

print_description_of_user('Den', 'AQ', 33, 'Male')
print_description_of_user(gender='Female', nickname='AQQQ', user_name='Alla')
print_description_of_user('Ivan', age=25)

