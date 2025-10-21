import sys
import pathlib

path_of_current_file = pathlib.Path(__file__)  # шлях до поточного файлу
path_to_base_folder = path_of_current_file.parent.parent

sys.path.insert(0, str(path_to_base_folder))

def collect_results():
    pass