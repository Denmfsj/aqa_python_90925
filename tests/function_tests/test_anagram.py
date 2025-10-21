import unittest

import sys
import pathlib

path_of_current_file = pathlib.Path(__file__)  # шлях до поточного файлу
path_to_base_folder = path_of_current_file.parent.parent.parent

sys.path.insert(0, str(path_to_base_folder))


import functions




class TestAnagram(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Getting data from .....')
        cls.user_data = [1,2,3]

    @classmethod
    def tearDownClass(cls):
        print('CleanUp data  .....')
        print(f'deleting {cls.user_data}')


    def setUp(self):
        print('\nbefore each test .....\n')


    def tearDown(self):
        print('\nafter each test .....\n')


    def test_anagram_true(self):

        actual_result = functions.is_anagram('anna', 'naan')
        print('test_anagram_true', self.user_data)

        self.assertTrue(actual_result)


    def test_anagram_false(self):

        actual_result = functions.is_anagram('Asd', 'asd')
        print('test_anagram_false', self.user_data)

        self.assertFalse(actual_result)



if __name__ == '__main__':  # виконай цей код якщо ти запустив цей файл
    unittest.main(verbosity=2)