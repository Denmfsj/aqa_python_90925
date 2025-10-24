import unittest

import sys
import pathlib
# print(sys.path)
#  '/home/den/hillel/aqa_python_90925', - знайти цей шлях

path_of_current_file = pathlib.Path(__file__)  # шлях до поточного файлу
path_to_base_folder = path_of_current_file.parent.parent.parent

# print('path_of_current_file -> ', path_of_current_file)
#  path_of_current_file ->  /home/den/hillel/aqa_python_90925/tests/function_tests/t_factorial.py

sys.path.insert(0, str(path_to_base_folder))


import functions




class TestFactorial(unittest.TestCase):


    def t_factorial_5(self):

        expected_result = 120
        actual_result = functions.factorial(5)

        self.assertEqual(expected_result, actual_result)


    def t_factorial_6(self):

        expected_result = 700
        actual_result = functions.factorial(6)

        self.assertAlmostEqual(expected_result, actual_result, delta=20)



    # def t_assert_diff(self):
    #
    #     users = [
    #         {'id': 18, 'name': 'alex'},
    #         {'id': 56, 'name': 'alex1'},
    #         {'id': 46, 'name': 'alex2'},
    #         {'id': 34, 'name': 'alex3'},
    #         {'id': 766, 'name': 'alex4'},
    #         {'id': 77, 'name': 'alex5'},
    #         {'id': 168, 'name': 'alex6'},
    #     ]
    #     users2 = [
    #         {'id': 18, 'name': 'alex'},
    #         {'id': 56, 'name': 'alex1'},
    #         {'id': 46, 'name': 'alex2'},
    #         {'id': 35, 'name': 'alex3'},
    #         {'id': 766, 'name': 'alex4'},
    #         {'id': 77, 'name': 'alex5'},
    #         {'id': 168, 'name': 'alex6'},
    #     ]
    #
    #     has_data = True
    #     has_errors = []
    #
    #     self.assertTrue(has_data)
    #     self.assertFalse(has_errors, f'Was found errors = {has_errors}')
    #
    #     self.assertGreater(10, 9)
    #     self.assertGreaterEqual(10, 10)
    #
    #     self.assertIn(1, [1,2,3])
    #     self.assertEqual(users, users2)




if __name__ == '__main__':  # виконай цей код якщо ти запустив цей файл
    unittest.main(verbosity=2)