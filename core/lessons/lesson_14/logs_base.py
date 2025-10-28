import logging
from definitions import BASE_PATH



# Налаштування конфігурації логування
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
logging.getLogger('').addHandler(console_handler)


file_handler = logging.FileHandler(BASE_PATH / 'errors_logs.txt')
file_handler.setLevel(logging.WARNING)
logging.getLogger('').addHandler(file_handler)


# Логування подій різного рівня
logging.debug('Це повідомлення рівня DEBUG')
logging.info('Це повідомлення рівня INFO')
logging.warning('Це повідомлення рівня WARNING')
logging.error('Це повідомлення рівня ERROR')
logging.critical('Це повідомлення рівня CRITICAL')