# try except finally

def connect():
    print('Connecting')
    return True

def execute(return_error=False):
    print('Executting ....')
    if return_error:
        raise ValueError('Cant execute query')

def close_connect():
    print('Close connection....')


try:
    connect()
    execute()

except Exception as e:  # e = змінна яка містить текст помилки
    print(f'Smth bad, error is {e}')

finally:
    close_connect()