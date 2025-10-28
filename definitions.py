import pathlib

BASE_PATH = pathlib.Path(__file__).parent
LOGS_PATH = pathlib.Path(__file__).parent / 'logs'
READ_WRITE_TEMP_FILE = BASE_PATH / 'resources'/ 'test_txt_data.txt'