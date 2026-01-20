import functions
import pytest
import time


time_data = [
        ('7:12 AM', '07:12'),
        ('12:00 AM', '00:00'),
        ('1:45 PM', '13:45'),
        ('11:59 PM', '23:59'),
    ]

@pytest.mark.time_converter
class TestDateConverter:

    @pytest.mark.smoke
    @pytest.mark.parametrize('input_data,expected', time_data)  # ('name', [values])
    def test_date_converter_smoke(self, input_data, expected):

        actual_result = functions.convert_to_24_hour(input_data)
        assert expected == actual_result



    @pytest.mark.slow
    @pytest.mark.regression
    def test_date_converter_regression(self):

        time.sleep(3)  # чекати 3 секунди

        expected_result = '19:00'
        actual_result = functions.convert_to_24_hour('7:00 PM')

        assert expected_result == actual_result
