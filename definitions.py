import pathlib

DEFINITION_FILE = pathlib.Path(__file__)

BASE_PATH = DEFINITION_FILE.parent

LOGS_PATH = BASE_PATH / 'logs'
READ_WRITE_TEMP_FILE = BASE_PATH / 'resources'/ 'temp' /'test_txt_data.txt'
SOME_DATA = pathlib.Path(str(BASE_PATH), 'folder_asd', "folder_2", 'file.txt')
TEMP_FOLDER = BASE_PATH / 'temp'
SCREENSHOTS_FOLDER = BASE_PATH / 'temp' / 'screenshots'
FILE_TO_READ_WRITE_LESSON_16 = BASE_PATH / 'core' /'lessons' / 'lesson_16' / 'some_text.txt'

SQLITE_DB = BASE_PATH / 'sqlite_db.db'



# print(DEFINITION_FILE.suffix)
# print(DEFINITION_FILE.name)

# print('Files')
# for el in BASE_PATH.iterdir():
#     if el.is_file() and el.suffix == '.log':
#         print(el)


# print(DEFINITION_FILE)
# print(READ_WRITE_TEMP_FILE)
# print(SOME_DATA)
#
# print('LOGS_PATH exists', LOGS_PATH.exists())
# print('READ_WRITE_TEMP_FILE exists', READ_WRITE_TEMP_FILE.exists())
# print(SCREENSHOTS_FOLDER)
# print('SCREENSHOTS_FOLDER exists', SCREENSHOTS_FOLDER.exists())
# SCREENSHOTS_FOLDER.mkdir(exist_ok=True, parents=True)
# print('SCREENSHOTS_FOLDER exists', SCREENSHOTS_FOLDER.exists())
#
# print('is folder DEFINITION_FILE', DEFINITION_FILE.is_dir())
# print('is file DEFINITION_FILE', DEFINITION_FILE.is_file())
# print('is folder BASE_PATH', BASE_PATH.is_dir())
# print('is file BASE_PATH', BASE_PATH.is_file())
#
# import shutil
#
# shutil.rmtree(SCREENSHOTS_FOLDER)