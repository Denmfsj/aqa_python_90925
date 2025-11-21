from datetime import date, datetime, timedelta


class DateTimeUtils:

    @staticmethod
    def get_current_date():
        return date.today()

    @staticmethod
    def get_difference_dt(original_dt: datetime = None, **kwargs):
        if original_dt is None:
            original_dt = datetime.now()
        return original_dt + timedelta(**kwargs)

    @staticmethod
    def get_current_quarter():
        return 4 # 1,2,3,4

    @staticmethod
    def get_days_between_dates(dt_1:datetime, dt_2:datetime):
        return (dt_1 - dt_2).days + 1

    @staticmethod
    def get_secs_between_dates(dt_1:datetime, dt_2:datetime):
        return (dt_1 - dt_2).total_seconds()

#
#
# def test_get_market_stat():
#
#     resposne = request.post(url,
#                             query_params={'date_from': DateTimeUtils.get_difference_dt(days=-7)})
