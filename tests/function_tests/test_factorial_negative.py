import unittest

import sys
import pathlib

from functions import factorial

# print(sys.path)
#  '/home/den/hillel/aqa_python_90925', - знайти цей шлях

path_of_current_file = pathlib.Path(__file__)  # шлях до поточного файлу
path_to_base_folder = path_of_current_file.parent.parent.parent

# print('path_of_current_file -> ', path_of_current_file)
#  path_of_current_file ->  /home/den/hillel/aqa_python_90925/tests/function_tests/test_factorial.py

sys.path.insert(0, str(path_to_base_folder))


import functions


def get_user_name():
    """Якщо нема user_name на сторінці"""
    raise TimeoutError('Cant fin element with xpath //div....')


class TestFactorial(unittest.TestCase):

    def test_user_name(self):

        with self.assertRaises(TimeoutError):
            get_user_name()

    def test_factorial_negative(self):

        with self.assertRaises(TypeError):
            functions.factorial('asds')




if __name__ == '__main__':  # виконай цей код якщо ти запустив цей файл
    unittest.main(verbosity=0)