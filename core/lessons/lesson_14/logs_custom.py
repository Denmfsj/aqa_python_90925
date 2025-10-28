import logging
from definitions import LOGS_PATH



api_logger = logging.getLogger('api service')
ui_logger = logging.getLogger('ui service')

api_logger.setLevel(logging.INFO)
ui_logger.setLevel(logging.INFO)

log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
base_format = logging.Formatter('%(name)s - %(message)s')

# файл для помилок  з API
api_file_error_handler  = logging.FileHandler(LOGS_PATH / 'api_error.log')
api_file_error_handler.setLevel(logging.ERROR)
api_file_error_handler.setFormatter(log_format)

# файл для помилок  з UI
ui_file_error_handler  = logging.FileHandler(LOGS_PATH / 'ui_error.log')
ui_file_error_handler.setLevel(logging.ERROR)
ui_file_error_handler.setFormatter(log_format)

# файл для всіх логів
log_file_handler = logging.FileHandler(LOGS_PATH / 'all_data.log')
log_file_handler.setLevel(logging.INFO)
log_file_handler.setFormatter(base_format)

# Додаемо ці
api_logger.addHandler(api_file_error_handler)
api_logger.addHandler(log_file_handler)

ui_logger.addHandler(ui_file_error_handler)
ui_logger.addHandler(log_file_handler)


def send_request():
    api_logger.info('Sending request to .....')
    api_logger.error('Cant get data from ...')

def open_page():
    ui_logger.info('Opening page ...')
    ui_logger.error('Cant open page ...')


send_request()
open_page()