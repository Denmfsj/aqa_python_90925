from datetime import datetime
from tzlocal import get_localzone
import pytz

now_without_tz = datetime.now()  # dt obj

some_time_str = '2025-11-21 16:13:11.259619'  # UTC? бо нема таймзони
some_time_with_tz_str = '2025-11-21 16:13:11.259619 +0100'

some_time_dt = datetime.fromisoformat(some_time_str)
some_time_with_tz_str = datetime.strptime(some_time_with_tz_str,
                                          '%Y-%m-%d %H:%M:%S.%f %z')

local_tz = str(get_localzone())
print(local_tz)
now_with_local_tz = pytz.timezone(local_tz).localize(now_without_tz)  # додати мою таймзону
now_with_utc_tz = pytz.timezone('UTC').localize(now_without_tz)  # додати UTC замість моєї таймзовни
some_time_dt_tz = pytz.timezone('UTC').localize(some_time_dt)


print(now_with_utc_tz)
print(now_with_local_tz)

print(now_with_utc_tz - now_with_local_tz)
