from datetime import datetime

time_string_1 = '2023-12-31 23:59:59'  # iso format

time_string_2 = '05-10-2025 23:59:59'
time_string_3 = '12-22-2025 23:59:59'
time_string_4 = '25-10-15T10:59:00 PM'   # y-m-d
time_string_5 = '25-10-15T10:59:00 PM +0900'
time_string_6 = '25-10-15'

dt_obj_2 = datetime.strptime(time_string_2, '%d-%m-%Y %H:%M:%S')  # зі строки в dt
dt_obj_3 = datetime.strptime(time_string_3, '%m-%d-%Y %H:%M:%S')  # зі строки в dt
dt_obj_4 = datetime.strptime(time_string_4, '%y-%m-%dT%I:%M:%S %p')  # зі строки в dt
dt_obj_5 = datetime.strptime(time_string_5, '%y-%m-%dT%I:%M:%S %p %z')  # зі строки в dt

dt_obj_6 = datetime.strptime(time_string_6, '%y-%m-%d')  # зі строки в dt

dt_5_string = dt_obj_5.strftime('%Y-%m-%d <-> %j. %H')
print(dt_5_string)


try:
    time_string_7 = '31-02-2024 23:59:59'
    datetime.strptime(time_string_7, '%d-%m-%Y %H:%M:%S')
except ValueError as e:
    raise AssertionError(f'Data from .... is invalid: {time_string_7} ->  {e}')

# dt_obj_1 = datetime.datetime.strftime()  # dt назад в строку
# print(dt_obj_5)
# print(dt_obj_5.year)
# print(dt_obj_5.date())
# print(dt_obj_5.day)
# print(dt_obj_5.hour)






