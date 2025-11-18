import random
import time

def retry(max_retries: int, error_type = Exception, delay=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0

            while retries < max_retries:
                try:
                    # Спроба виклику функції, яку декоруємо
                    return func(*args, **kwargs)
                except error_type as e:
                    # Обробка помилки та вивід повідомлення про спробу
                    print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
                    retries += 1

                    if delay > 0:
                        time.sleep(delay)

            # Викидаємо виняток, якщо досягнуто максимальну кількість спроб
            raise Exception("Досягнуто максимальну кількість спроб")
        return wrapper
    return decorator


# Параметризоване застосування декоратора
@retry(max_retries=3, error_type=ConnectionError, delay=1)
def connect_to_server():
    # Спроба з'єднатися з сервером
    # example1111.com
    raise ConnectionError("Не вдалося підключитися до сервера")



# Параметризоване застосування декоратора
@retry(max_retries=5, error_type=AttributeError)
def calculate_current_time():
    if random.choice(range(10)) < 5:
        raise AttributeError("Cant get current time")
    return 'now'

# connect_to_server()
print(calculate_current_time())