import time
import random


class GetApiUserDetails:
    """Класс який буде повертати деталі юзерів по 1"""

    def __init__(self, number_of_users, mode='random'):
        self.__number = number_of_users
        self.__current_number_of_user = 0
        self.__user_id = None
        self.__user_ids = range(10, 100001)

        if mode in ['random', 'sorted_by_date']:
            self.__mode=mode
        else:
            raise AttributeError(f'unknown mode {mode}')

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_number_of_user < self.__number:
            if self.__mode == 'random':
                self.__user_id = None
            else:

                self.__user_id = self.__user_ids[-1 - self.__current_number_of_user]

            user = self.__get_user_detail(self.__user_id)

            self.__current_number_of_user += 1
            return user
        else:
            raise StopIteration

    def __get_user_detail(self, user_id=None):
        """Посилаю запит і отримую випадкового юзера"""
        if user_id is None:
            user_id = random.choice(self.__user_ids) # обирати випадкоий user_id

        print(f'Sending request to users/{user_id}/details')
        time.sleep(1)  # очікувати 1 секунду
        return {'id': user_id, 'name': 'Alex', 'is_valid': True}



def test_check_user_are_valid():
    """Я хочу брати випадкових 10 юзерів"""
    for k in GetApiUserDetails(10, mode='random'):
        print(f'testing of {k}')
        assert k['is_valid'] == True



def test_user_have_valid_names():
    """Я хочу брати останні 10 юзерів які зареестровані і первіряти, що імена не порожні"""
    for k in GetApiUserDetails(10, mode='sorted_by_date'):
        print(f'testing of {k}')
        assert len(k['name']) > 0



def test_broken():
    """Я хочу брати останні 10 юзерів які зареестровані і первіряти, що імена не порожні"""
    for k in GetApiUserDetails(10, mode='asd'):
        print(f'testing of {k}')
        assert len(k['name']) > 0

#
# class CustomeIter():
#     ....
#
# for k in CustomeIter([1,2,3]):
#     print(k)  # три ітерації: 3,  2, 1