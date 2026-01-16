from datetime import datetime, timedelta
import pytz
from tzlocal import get_localzone


now_without_tz = datetime.now()  # dt obj

some_time_str = '2025-11-01 16:13:11.259619'
some_time_dt = datetime.fromisoformat(some_time_str)

diff = now_without_tz - some_time_dt

print(now_without_tz + timedelta(minutes=-55555, days=1))
print(some_time_dt - now_without_tz)




# print(diff)
# print(diff.days)
# print(diff.seconds)
# print(diff.microseconds)
# print(diff.total_seconds())


# def test_check_history_buc():
#
#     # add_to_basket()
#     start_time = pytz.timezone(str(get_localzone())).localize(datetime.now()) # dt з таймзоною
#     # checkout()
#     # get_history_of_item()
#     # history_from_api = get_history_of_item()
#     time_of_buy = datetime.fromisoformat('2025-11-15 16:13:11.259619')  # history_from_api['created_date']
#
#
#     diff = time_of_buy - start_time
#     assert diff.total_seconds() < 60, "Time from start checkout to end of processing MUST be < 60 sec"
#
#     # end_time =  pytz.timezone(str(get_localzone())).localize(datetime.now())
#     # assert time_of_buy < end_time  # не пізніше ніж зараз
#     # assert time_of_buy > start_time  # не раніше старту теста