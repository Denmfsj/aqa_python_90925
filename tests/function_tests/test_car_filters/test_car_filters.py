import pytest

from tests.function_tests.test_car_filters.positive_cases import *


@pytest.mark.parametrize('filter_data, expected_result', [
    ((2020, 2, 50000), filter_2020_20_50000),
    ((2010, 1, 30000), filter_2010_10_30000),
])
def test_filter_of_cars(filter_data, expected_result):

    actual_result = sorted_cars(filter_data)
    assert expected_result == actual_result


@pytest.mark.parametrize('company_id', [200, 473, 654])
def test_base_info_about_company(company_id):

    get_data_from_api(company_id)