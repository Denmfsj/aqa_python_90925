import functions
import pytest
from definitions import READ_WRITE_TEMP_FILE


@pytest.fixture
def check_smth_before_test():
    create_user_id = 314
    print('\n!!!!!!!!!!!!!!Pre condition for each test!!!!!!!!!!!!!!!!!\n')
    yield create_user_id
    print('\n!!!!!!!!!!!!!!POST condition for each test!!!!!!!!!!!!!!!!!\n')
    print(f'Deleting user {create_user_id}')

@pytest.mark.smoke
@pytest.mark.triangle_feature
@pytest.mark.parametrize('number1, number2, number3, expected', [
    (12, 20, 30, 80.49223565040295),
    (1, 1, 1, 0.4330127018922193),
])
def __test_triangle_area_smoke(number1, number2, number3, expected, check_smth_before_test):
    print(check_smth_before_test)
    actual_result = functions.triangle_area(number1, number2, number3)

    assert expected == actual_result


@pytest.mark.parametrize('sort_by', ['d_day', 'reg_day'])
@pytest.mark.parametrize('age', [18, 30, 40, 60])
def test_check_age_and_name(age, sort_by):
    print(f'Users sorted by  {sort_by} age is {age}')

