import os
from definitions import BASE_PATH
import pathlib

# os.system('ls -la')


# for item in os.walk(BASE_PATH):
#     start_folder = item[0]  # шлях до папки
#     list_of_folders = item[1]  # імена папок в start_folder
#     list_of_files = item[2]  # імена файлі в  start_folder

for start_folder, list_of_folders, list_of_files in os.walk(BASE_PATH):
 ## /home/den/hillel/aqa_python_90925/core, ['api', 'lessons', 'ui'], ['__init__.py', 'functions_copy.py']
    for file_name in list_of_files:
        if file_name.endswith('.log'):
            print(pathlib.Path(start_folder, file_name))

