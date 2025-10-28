import logging

def factorial(n):

    if n < 0:
        raise ValueError(f'You have to use 0 or positive numbers. You put {n}')

    if type(n) != int:
        raise TypeError(f'Only int allowed, you put {type(n)}')

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_anagram(word1, word2):
    """
    description
    """
    return sorted(word1) == sorted(word2)


def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]


def find_primes(n: int) -> list:
    logging.info(f'find_primes was called with {n}, {type(n)}')
    logging.debug(f'find_primes was called with debug level  {n}, {type(n)}')
    logging.critical(f'find_primes was called with critical level  {n}, {type(n)}')

    if type(n) != int:
        logging.error(f'find_primes input param is not int {type(n)}, {n}')


    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def triangle_area(a, b, c):
    # if a + b <= c or a + c <= b or b + c <= a:
    #     return 0
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def convert_to_24_hour(time_str):

    if type(time_str) == list:
        raise TypeError

    if type(time_str) == dict:
        raise ValueError

    parts = time_str.split()
    if len(parts) != 2:
        raise ValueError('Time format is not a `hh:mm period`')
    time, period = parts
    hours, minutes = map(int, time.split(':'))
    if period.lower() == 'pm' and hours != 12:
        hours += 12
    elif period.lower() == 'am' and hours == 12:
        hours = 0
    return f'{hours:02}:{minutes:02}'



if __name__ == '__main__':
    print('''asd''')