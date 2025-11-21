import time
import datetime

start_time = time.time()
# time.sleep(1.5)  # півтри секунди очікеування
# print(time.time() - start_time)
# print(time.time())  # 1763745702.1912405 - кількість міліскваунда з 1.1.70
#
# print(datetime.datetime.fromtimestamp(1763745702.1912405))
#
# def test_check_history_buc():
#     start_time =  time.time()
#     # add_to_bucket()
#     # checkout()
#     # get_history_of_item()
#     history_from_api = get_history_of_item()
#     time_of_buy = history_from_api['created_date']
#     assert time_of_buy < time.time()  # не пізніше ніж зараз
#     assert time_of_buy > start_time  # не раніше старту теста

cur_time = time.localtime()

print(cur_time)
print(cur_time.tm_hour)
print(cur_time.tm_min)
print(cur_time.tm_zone)
print(cur_time.tm_wday)
print(cur_time.tm_mday)