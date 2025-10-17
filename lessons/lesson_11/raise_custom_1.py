# try except finally
import time

msg_id = 123  # діcтав від сервера


time_to_wait = 10
start_time = time.time()

while True:

    server_answer = False  # посилаю запит до сервера і перевіряю відпвідь

    if time.time() - start_time > 10:
        print('Wait too long')
        raise NameError(f'Cant get answer for msg_id={msg_id} for {time_to_wait} seconds')
    print('Waiting')
    time.sleep(1)  # чекати 1 секунду

