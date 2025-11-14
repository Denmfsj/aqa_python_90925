import functions
import pytest
from definitions import READ_WRITE_TEMP_FILE

# pre-condition = create user
# test = change user
# post-condition = delete user

# pre-condition = create user
# test = get user
# test = change user
# post-condition = delete user



@pytest.mark.smoke
@pytest.mark.triangle_feature
def test_triangle_area_smoke():

    expected_result = 80.49223565040295
    actual_result = functions.triangle_area(12,20,30)

    with open(READ_WRITE_TEMP_FILE) as f:
        f.read()

    assert expected_result == actual_result


@pytest.mark.triangle_feature
@pytest.mark.xfail(reason='Flaky issue = JIRA-111')
def test_triangle_area_1_1_1():
    expected_result = 0.4330127018922193
    actual_result = functions.triangle_area(1,1,1)

    assert expected_result == actual_result

@pytest.mark.regression
@pytest.mark.triangle_feature
def test_triangle_area_regression():

    expected_result = 80.49
    actual_result = functions.triangle_area(12,20,30)
    actual_result_round = round(actual_result, 2)  # round(number, number_after_dot)

    assert expected_result == actual_result_round
