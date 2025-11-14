import time
import random


def check_time_execution(fn):  # fn - функція

    def wrapper(*args, **kwargs):  # wrapper - ім'я функції, *args, **kwargs - приймає будь-які аргументи
        print(f'{fn.__name__} is called with args: {args}  and kwargs {kwargs}')
        start_time = time.time()
        res = fn(*args, **kwargs)  # send_request('user/api', query_params={'sort_by': '-date_reg'})
        time_execution = time.time() - start_time
        print(fn.__name__, time_execution)

        return res

    return wrapper



@check_time_execution
def send_request(url, query_params=None):
    time.sleep(random.choice(range(100, 300))/100)  # чекати 1-3 секунди
    pass

@check_time_execution
def get_data_from_db(user_id):
    time.sleep(random.choice(range(100, 200))/100)  # чекати 1-2 секунди
    pass

@check_time_execution
def open_home_page(url=None):
    time.sleep(random.choice(range(1, 100))/100)  # чекати до 1 секунди
    pass


open_home_page()
get_data_from_db(123)
send_request('user/api', query_params={'sort_by': '-date_reg'})