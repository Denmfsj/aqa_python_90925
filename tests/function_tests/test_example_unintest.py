import unittest


class TestExample(unittest.TestCase):


    def test_first_example(self):

        expected_result = 'Den'
        actual_result = 'Den'

        self.assertEqual(expected_result,actual_result)


    def test_first_example_broken(self):

        expected_result = 'Den'
        actual_result = 'Den2'

        # assert expected_result == actual_result, f'Name from api should be {expected_result} but its not'

        self.assertEqual(expected_result, actual_result,
                         f'Name from api should be {expected_result} but its not')

print('value of __name__ =',__name__)

if __name__ == '__main__':  # виконай цей код якщо ти запустив цей файл
    unittest.main()