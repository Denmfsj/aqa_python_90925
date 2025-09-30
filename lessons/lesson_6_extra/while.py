import random
import time



# number = 21
# while number > 5:  # поки номер більше 5
#
#     print(f'Number is {number}')
#     number = random.choice(range(20))  # обирати випадкове число від 0 до 19

# print('Done')

# чекати позитивної відповіді від сервера не більеш 10 секунд

server_response = None
time_to_wait = 10
delta_time = 1  # як часто посилати запити на сервер
start_time = time.time()  # поточний час в ms починаючи з 1.1.1970


while True:  # вічний цикл
    server_response = random.choice(range(100))  # range(100) = список від 0 до 99
    # random.choice обрати щось 1 зі списоку, слвника і тд
    print(f'Response is {server_response}')

    if server_response >= 95:
        print('Response is good')
        break  # розриваю цикл while бо сервер прислав гарну відповідь

    # чи ен вийшов час очікування
    time_pass = time.time() - start_time
    print(f'{time_pass}')

    if time_pass > time_to_wait:
        print('Break because wait time > 10 sec')
        break  # розриваю цикл while бо time_to_wait  секунд


    time.sleep(delta_time)  # чекати delta_time секунд

print('Done')


