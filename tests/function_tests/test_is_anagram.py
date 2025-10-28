import pytest
from functions import is_anagram
import logging
# from definitions import BASE_PATH

# function_file = BASE_PATH / 'core' / 'functions_copy.py'
#
# print(str(function_file))




@pytest.mark.parametrize('word1, word2, expected', [
    ('den', 'ned', True),
    ('den', 'dden', True),
    ('', '', True),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'a', False),
])
def test_is_anagram(word1, word2, expected):

    logging.info(f'Run test with params: {word1}, {word2}')
    actual_result = is_anagram(word1, word2)
    assert expected == actual_result, \
        f'{word1} is anagram of {word2}: it it {expected}, but actual res is {actual_result}'
#
